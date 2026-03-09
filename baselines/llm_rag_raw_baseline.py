"""
RAG baseline using RAW enterprise documents (not oracle context).

Parses messy enterprise documents with multi-hop challenge:
- Runbooks (Markdown) - Source → Intermediate Code mappings
- Email threads (Text) - IC → Target mappings + temporal contradictions
- Wiki pages (Markdown) - Implicit relationships
- Slack exports (JSON) - Casual mentions, noise
- Policy documents (Markdown) - Dense compliance docs

NOTE: Spreadsheets are intentionally excluded as they contained oracle-like
direct entity ID mappings that bypass the multi-hop challenge.
"""
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import math
from collections import Counter


@dataclass
class DocumentChunk:
    """A chunk from a raw document."""
    doc_id: str
    doc_type: str
    text: str
    source_file: str


def tokenize(text: str) -> List[str]:
    """Simple tokenization."""
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    stop_words = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'to', 'of', 'in',
                  'for', 'on', 'with', 'as', 'by', 'at', 'from', 'and', 'or'}
    return [t for t in tokens if t not in stop_words and len(t) > 1]


class BM25Index:
    """BM25-based index for document retrieval."""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.chunks: List[DocumentChunk] = []
        self.doc_freqs: Dict[str, int] = {}
        self.doc_lens: List[int] = []
        self.avgdl: float = 0.0
        self.doc_tokens: List[List[str]] = []
        self.N: int = 0

    def build_index(self, chunks: List[DocumentChunk]):
        """Build the BM25 index."""
        self.chunks = chunks
        self.N = len(chunks)
        self.doc_tokens = []
        self.doc_lens = []

        print(f"Building BM25 index for {len(chunks)} raw document chunks...")

        for chunk in chunks:
            tokens = tokenize(chunk.text)
            self.doc_tokens.append(tokens)
            self.doc_lens.append(len(tokens))

            for token in set(tokens):
                self.doc_freqs[token] = self.doc_freqs.get(token, 0) + 1

        self.avgdl = sum(self.doc_lens) / len(self.doc_lens) if self.doc_lens else 0
        print(f"Index built. Vocabulary size: {len(self.doc_freqs)}")

    def _score(self, query_tokens: List[str], doc_idx: int) -> float:
        """Calculate BM25 score."""
        score = 0.0
        doc_tokens = self.doc_tokens[doc_idx]
        doc_len = self.doc_lens[doc_idx]
        term_freqs = Counter(doc_tokens)

        for token in query_tokens:
            if token not in self.doc_freqs:
                continue
            df = self.doc_freqs[token]
            idf = math.log((self.N - df + 0.5) / (df + 0.5) + 1)
            tf = term_freqs.get(token, 0)
            denom = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
            score += idf * (tf * (self.k1 + 1)) / denom
        return score

    def search(self, query: str, top_k: int = 10) -> List[Tuple[DocumentChunk, float]]:
        """Search for relevant chunks."""
        query_tokens = tokenize(query)
        if not query_tokens:
            return []

        scores = []
        for idx in range(self.N):
            score = self._score(query_tokens, idx)
            if score > 0:
                scores.append((idx, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return [(self.chunks[idx], score) for idx, score in scores[:top_k]]


def load_markdown_documents(raw_dir: Path, subdir: str) -> List[DocumentChunk]:
    """Load and chunk Markdown documents."""
    chunks = []
    md_dir = raw_dir / subdir

    if not md_dir.exists():
        return chunks

    for md_file in md_dir.glob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split into sections by headers
            sections = re.split(r'\n#{1,3}\s+', content)

            for i, section in enumerate(sections):
                if len(section.strip()) > 50:  # Skip very short sections
                    chunks.append(DocumentChunk(
                        doc_id=f"{md_file.stem}_{i}",
                        doc_type=subdir.replace('_', ''),
                        text=section[:2000],  # Limit chunk size
                        source_file=str(md_file.name)
                    ))
        except Exception as e:
            print(f"Warning: Could not parse {md_file}: {e}")

    return chunks


def load_email_documents(raw_dir: Path) -> List[DocumentChunk]:
    """Load email threads."""
    chunks = []
    email_dir = raw_dir / "email_threads"

    if not email_dir.exists():
        return chunks

    for email_file in email_dir.glob("*.txt"):
        try:
            with open(email_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split by email boundaries
            emails = re.split(r'\n-{3,}\n', content)

            for i, email in enumerate(emails):
                if len(email.strip()) > 50:
                    chunks.append(DocumentChunk(
                        doc_id=f"{email_file.stem}_{i}",
                        doc_type="email",
                        text=email[:2000],
                        source_file=str(email_file.name)
                    ))
        except Exception as e:
            print(f"Warning: Could not parse {email_file}: {e}")

    return chunks


def load_slack_documents(raw_dir: Path) -> List[DocumentChunk]:
    """Load Slack exports."""
    chunks = []
    slack_dir = raw_dir / "slack_exports"

    if not slack_dir.exists():
        return chunks

    for slack_file in slack_dir.glob("*.json"):
        try:
            with open(slack_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            messages = data.get("messages", [])
            for i, msg in enumerate(messages):
                text = msg.get("text", "")
                if len(text) > 20:
                    chunks.append(DocumentChunk(
                        doc_id=f"{slack_file.stem}_{i}",
                        doc_type="slack",
                        text=text,
                        source_file=str(slack_file.name)
                    ))
        except Exception as e:
            print(f"Warning: Could not parse {slack_file}: {e}")

    return chunks


def load_all_raw_documents(raw_dir: Path) -> List[DocumentChunk]:
    """Load all raw documents for multi-hop RAG evaluation.

    Loads unstructured enterprise documents that require multi-hop reasoning
    to resolve entity mappings. Spreadsheets are excluded as they contained
    oracle-like direct entity ID mappings.
    """
    all_chunks = []

    print("Loading raw documents (multi-hop challenge)...")

    # Runbooks - Source → Intermediate Code mappings
    runbook_chunks = load_markdown_documents(raw_dir, "migration_runbooks")
    print(f"  Runbooks: {len(runbook_chunks)} chunks")
    all_chunks.extend(runbook_chunks)

    # Wiki pages - Implicit relationships
    wiki_chunks = load_markdown_documents(raw_dir, "wiki_pages")
    print(f"  Wiki pages: {len(wiki_chunks)} chunks")
    all_chunks.extend(wiki_chunks)

    # Policy documents
    policy_chunks = load_markdown_documents(raw_dir, "policy_documents")
    print(f"  Policy docs: {len(policy_chunks)} chunks")
    all_chunks.extend(policy_chunks)

    # Emails - IC → Target mappings + temporal contradictions
    email_chunks = load_email_documents(raw_dir)
    print(f"  Emails: {len(email_chunks)} chunks")
    all_chunks.extend(email_chunks)

    # Slack - Noise + occasional relevant info
    slack_chunks = load_slack_documents(raw_dir)
    print(f"  Slack: {len(slack_chunks)} chunks")
    all_chunks.extend(slack_chunks)

    print(f"Total: {len(all_chunks)} chunks")
    return all_chunks


class RawRAGRetrieval:
    """RAG retrieval using raw documents."""

    def __init__(self, top_k: int = 10):
        self.top_k = top_k
        self.index = BM25Index()
        self.initialized = False

    def initialize(self, raw_dir: Path):
        """Initialize from raw documents directory."""
        chunks = load_all_raw_documents(raw_dir)
        self.index.build_index(chunks)
        self.initialized = True

    def get_context(self, entity_a: Dict, entity_b: Dict) -> str:
        """Retrieve relevant context for an entity pair."""
        if not self.initialized:
            return "RAG index not initialized."

        # Build query from entity attributes
        parts = []
        for entity in [entity_a, entity_b]:
            name = entity.get("name", "")
            system = entity.get("source_system", "")
            attrs = entity.get("attributes", {})
            internal_code = attrs.get("internal_code", "")
            category = attrs.get("category", "")

            parts.append(f"{name} {system} {internal_code} {category}")

        query = " ".join(parts)
        results = self.index.search(query, top_k=self.top_k)

        if not results:
            return "No relevant context found."

        context_lines = []
        for chunk, score in results:
            context_lines.append(f"[{chunk.doc_type.upper()}] {chunk.text[:500]}")

        return "RELEVANT CONTEXT (from raw documents):\n" + "\n\n".join(context_lines)


def build_prompt(entity_a: Dict, entity_b: Dict, context: str = "") -> str:
    """Build the classification prompt."""
    entity_a_str = json.dumps(entity_a, indent=2)
    entity_b_str = json.dumps(entity_b, indent=2)

    prompt = f"""You are an entity resolution system. Determine if these two entity records refer to the same real-world entity.

ENTITY A:
{entity_a_str}

ENTITY B:
{entity_b_str}
"""

    if context:
        prompt += f"""
AUXILIARY CONTEXT:
{context}
"""

    prompt += """
Based on the entity attributes""" + (" and available context" if context else "") + """, classify this pair.

Respond with exactly one word: MATCH, NO_MATCH, or AMBIGUOUS"""

    return prompt


def parse_response(response: str) -> str:
    """Parse LLM response to label."""
    response = response.upper().strip()
    if "MATCH" in response and "NO_MATCH" not in response and "NO MATCH" not in response:
        return "match"
    elif "NO_MATCH" in response or "NO MATCH" in response:
        return "no_match"
    elif "AMBIGUOUS" in response:
        return "ambiguous"
    return "no_match"


def run_raw_rag_baseline(
    data_dir: Path,
    api_key: str,
    model: str = "claude-sonnet-4-20250514",
    top_k: int = 10,
    split: str = "test",
    limit: Optional[int] = None
) -> Dict[str, Any]:
    """Run RAG baseline with raw documents."""
    import anthropic

    client = anthropic.Anthropic(api_key=api_key)

    # Load dataset
    with open(data_dir / "crosser_dataset.json") as f:
        dataset = json.load(f)

    entities = {e["entity_id"]: e for e in dataset["entities"]}
    pairs = [p for p in dataset["pairs"] if p["split"] == split]

    if limit:
        pairs = pairs[:limit]

    # Initialize RAG with raw documents
    raw_dir = data_dir / "context" / "raw"
    rag = RawRAGRetrieval(top_k=top_k)
    rag.initialize(raw_dir)

    print(f"\nRunning RAW RAG (top-{top_k}) baseline on {len(pairs)} {split} pairs...")
    print(f"Using model: {model}")

    predictions = []
    correct = 0

    for i, pair in enumerate(pairs):
        entity_a = entities[pair["entity_a"]]
        entity_b = entities[pair["entity_b"]]

        ctx = rag.get_context(entity_a, entity_b)
        prompt = build_prompt(entity_a, entity_b, ctx)

        response = client.messages.create(
            model=model,
            max_tokens=50,
            messages=[{"role": "user", "content": prompt}]
        )

        predicted = parse_response(response.content[0].text)

        predictions.append({
            "pair_id": pair["pair_id"],
            "predicted_label": predicted,
            "actual_label": pair["label"],
            "context_mechanism": f"raw_rag_top{top_k}"
        })

        if predicted == pair["label"]:
            correct += 1

        if (i + 1) % 10 == 0:
            print(f"  Processed {i + 1}/{len(pairs)} (acc so far: {correct/(i+1):.3f})")

    accuracy = correct / len(pairs) if pairs else 0
    print(f"  Final accuracy: {accuracy:.3f}")

    # Calculate metrics
    tp = sum(1 for p in predictions
             if p["predicted_label"] == "match" and p["actual_label"] == "match")
    fp = sum(1 for p in predictions
             if p["predicted_label"] == "match" and p["actual_label"] != "match")
    fn = sum(1 for p in predictions
             if p["predicted_label"] != "match" and p["actual_label"] == "match")

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    results = {
        "predictions": predictions,
        "metrics": {
            "provider": "anthropic",
            "model": model,
            "mechanism": f"raw_rag_top{top_k}",
            "accuracy": round(accuracy, 4),
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
            "total_pairs": len(pairs)
        }
    }

    print(f"\nRAW RAG (top-{top_k}): P={precision:.3f}, R={recall:.3f}, F1={f1:.3f}")
    return results


def main():
    """Run RAW RAG baseline."""
    import argparse

    parser = argparse.ArgumentParser(description="Run RAW RAG baseline for CrossER")
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).parent.parent / "data")
    parser.add_argument("--results-dir", type=Path, default=Path(__file__).parent / "results")
    parser.add_argument("--api-key", type=str, required=True, help="Anthropic API key")
    parser.add_argument("--model", type=str, default="claude-sonnet-4-20250514")
    parser.add_argument("--top-k", type=int, default=10, help="Number of chunks to retrieve")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of pairs")

    args = parser.parse_args()
    args.results_dir.mkdir(parents=True, exist_ok=True)

    results = run_raw_rag_baseline(
        data_dir=args.data_dir,
        api_key=args.api_key,
        model=args.model,
        top_k=args.top_k,
        limit=args.limit
    )

    output_name = f"llm_anthropic_raw_rag_top{args.top_k}.json"
    with open(args.results_dir / output_name, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {args.results_dir / output_name}")


if __name__ == "__main__":
    main()

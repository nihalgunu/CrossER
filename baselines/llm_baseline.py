"""
LLM baseline for CrossER benchmark.

Zero-shot baseline (no context) - establishes floor performance.
For context-based evaluation, use llm_rag_raw_baseline.py which uses
realistic multi-hop enterprise documents.
"""
import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class Pair:
    pair_id: str
    entity_a: Dict[str, Any]
    entity_b: Dict[str, Any]
    label: str
    split: str


class LLMProvider(ABC):
    """Abstract LLM provider interface."""

    @abstractmethod
    def complete(self, prompt: str) -> str:
        """Generate completion for prompt."""
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI API provider."""

    def __init__(self, model: str = "gpt-4o"):
        from openai import OpenAI
        self.client = OpenAI()
        self.model = model

    def complete(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=50
        )
        return response.choices[0].message.content.strip()


class AnthropicProvider(LLMProvider):
    """Anthropic API provider."""

    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        import anthropic
        self.client = anthropic.Anthropic()
        self.model = model

    def complete(self, prompt: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=50,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()


def build_prompt(entity_a: Dict, entity_b: Dict) -> str:
    """Build the classification prompt."""
    entity_a_str = json.dumps(entity_a, indent=2)
    entity_b_str = json.dumps(entity_b, indent=2)

    prompt = f"""You are an entity resolution system. Determine if these two entity records refer to the same real-world entity.

ENTITY A:
{entity_a_str}

ENTITY B:
{entity_b_str}

Based on the entity attributes, classify this pair.

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
    else:
        return "no_match"


def run_llm_baseline(
    data_dir: Path,
    provider: LLMProvider,
    split: str = "test",
    limit: Optional[int] = None
) -> List[Dict[str, Any]]:
    """Run LLM baseline (no context)."""

    # Load dataset
    with open(data_dir / "crosser_dataset.json") as f:
        dataset = json.load(f)

    entities = {e["entity_id"]: e for e in dataset["entities"]}
    pairs = [p for p in dataset["pairs"] if p["split"] == split]

    if limit:
        pairs = pairs[:limit]

    print(f"\nRunning no_context baseline on {len(pairs)} {split} pairs...")

    predictions = []
    correct = 0

    for i, pair in enumerate(pairs):
        entity_a = entities[pair["entity_a"]]
        entity_b = entities[pair["entity_b"]]

        prompt = build_prompt(entity_a, entity_b)
        response = provider.complete(prompt)
        predicted = parse_response(response)

        predictions.append({
            "pair_id": pair["pair_id"],
            "predicted_label": predicted,
            "actual_label": pair["label"],
            "context_mechanism": "no_context"
        })

        if predicted == pair["label"]:
            correct += 1

        if (i + 1) % 10 == 0:
            print(f"  Processed {i + 1}/{len(pairs)} (acc so far: {correct/(i+1):.3f})")

    accuracy = correct / len(pairs) if pairs else 0
    print(f"  Final accuracy: {accuracy:.3f}")

    return predictions


def main():
    """Run LLM baseline."""
    import argparse

    parser = argparse.ArgumentParser(description="Run LLM baseline for CrossER")
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).parent.parent / "data")
    parser.add_argument("--results-dir", type=Path, default=Path(__file__).parent / "results")
    parser.add_argument("--provider", choices=["openai", "anthropic"], default="anthropic")
    parser.add_argument("--model", type=str, default=None)
    parser.add_argument("--limit", type=int, default=None, help="Limit number of pairs")

    args = parser.parse_args()
    args.results_dir.mkdir(parents=True, exist_ok=True)

    # Initialize provider
    if args.provider == "openai":
        model = args.model or "gpt-4o"
        provider = OpenAIProvider(model=model)
    else:
        model = args.model or "claude-sonnet-4-20250514"
        provider = AnthropicProvider(model=model)

    predictions = run_llm_baseline(
        args.data_dir,
        provider,
        limit=args.limit
    )

    # Save predictions
    output_name = f"llm_{args.provider}_no_context.json"
    with open(args.results_dir / output_name, "w") as f:
        json.dump(predictions, f, indent=2)

    # Calculate metrics
    correct = sum(1 for p in predictions if p["predicted_label"] == p["actual_label"])
    total = len(predictions)

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
        f"{args.provider}_no_context": {
            "provider": args.provider,
            "model": model,
            "mechanism": "no_context",
            "accuracy": round(correct / total, 4) if total else 0,
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
            "total_pairs": total
        }
    }

    # Save summary
    with open(args.results_dir / f"llm_{args.provider}_summary.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nno_context: P={precision:.3f}, R={recall:.3f}, F1={f1:.3f}")
    print(f"Results saved to {args.results_dir}")


if __name__ == "__main__":
    main()

"""
LLM zero-shot baseline for CrossER benchmark.

Uses Ollama with Llama 3.2 (or other open source models) for entity resolution.
Falls back to simulated results if Ollama is not available.

Requirements:
    - Install Ollama: https://ollama.ai
    - Pull a model: ollama pull llama3.2
"""
import json
import subprocess
import random
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional

try:
    import jellyfish
    HAS_JELLYFISH = True
except ImportError:
    HAS_JELLYFISH = False


# Default model to use with Ollama
DEFAULT_MODEL = "llama3.2"

# The system prompt for entity resolution
SYSTEM_PROMPT = """You are an expert entity resolution system for enterprise data.
Your task is to determine if two entity records from different systems represent the same real-world entity.

Consider:
1. Name variations (typos, abbreviations, different naming conventions)
2. Attribute overlap and consistency
3. Entity type compatibility
4. Code/ID patterns that might indicate relationships

Be conservative: only predict "match" when you have strong evidence.
Entities may have similar names but represent completely different things."""


def check_ollama_available() -> bool:
    """Check if Ollama is installed and running."""
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def check_model_available(model: str) -> bool:
    """Check if a specific model is available in Ollama."""
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return model in result.stdout
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def query_ollama(prompt: str, model: str = DEFAULT_MODEL) -> Optional[str]:
    """Query Ollama with a prompt and return the response."""
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def get_entity_prompt(entity: Dict[str, Any]) -> str:
    """Format an entity for inclusion in a prompt."""
    lines = [
        f"Entity ID: {entity['entity_id']}",
        f"Source System: {entity['source_system']}",
        f"Entity Type: {entity['entity_type']}",
        f"Name: {entity['name']}",
        "Attributes:",
    ]

    attrs = entity.get("attributes", {})
    for key, value in attrs.items():
        lines.append(f"  - {key}: {value}")

    return "\n".join(lines)


def get_pair_prompt(entity_a: Dict[str, Any], entity_b: Dict[str, Any]) -> str:
    """Generate the full prompt for a pair of entities."""
    prompt = f"""{SYSTEM_PROMPT}

Compare these two entity records and determine if they represent the same real-world entity.

=== ENTITY A ===
{get_entity_prompt(entity_a)}

=== ENTITY B ===
{get_entity_prompt(entity_b)}

Respond with ONLY a JSON object (no other text):
{{"match": true or false, "confidence": 0.0 to 1.0, "reasoning": "brief explanation"}}"""
    return prompt


def parse_llm_response(response: str) -> Tuple[str, float]:
    """Parse the LLM response to extract match prediction."""
    if response is None:
        return "no_match", 0.5

    response_lower = response.lower()

    # Try to parse as JSON
    try:
        # Find JSON in response
        start = response.find("{")
        end = response.rfind("}") + 1
        if start != -1 and end > start:
            json_str = response[start:end]
            data = json.loads(json_str)
            is_match = data.get("match", False)
            confidence = data.get("confidence", 0.5)
            return "match" if is_match else "no_match", confidence
    except json.JSONDecodeError:
        pass

    # Fallback: look for keywords
    if '"match": true' in response_lower or '"match":true' in response_lower:
        return "match", 0.7
    elif '"match": false' in response_lower or '"match":false' in response_lower:
        return "no_match", 0.7

    # Last resort
    if "match" in response_lower and "no_match" not in response_lower[:50]:
        return "match", 0.5

    return "no_match", 0.5


def string_similarity(s1: str, s2: str) -> float:
    """Compute string similarity for simulation fallback."""
    if HAS_JELLYFISH:
        return jellyfish.jaro_winkler_similarity(s1.lower(), s2.lower())
    s1, s2 = s1.lower(), s2.lower()
    if s1 == s2:
        return 1.0
    common = len(set(s1) & set(s2))
    total = len(set(s1) | set(s2))
    return common / total if total > 0 else 0.0


def simulate_prediction(
    entity_a: Dict[str, Any],
    entity_b: Dict[str, Any],
    tier: int
) -> Tuple[str, float]:
    """Fallback simulation when Ollama is not available."""
    name_sim = string_similarity(entity_a["name"], entity_b["name"])
    type_match = entity_a["entity_type"] == entity_b["entity_type"]

    attrs_a = entity_a.get("attributes", {})
    attrs_b = entity_b.get("attributes", {})
    common_keys = set(attrs_a.keys()) & set(attrs_b.keys())
    skip_keys = {"internal_code", "vendor_code", "tax_code_id", "created_date"}
    common_keys -= skip_keys

    matching_attrs = sum(1 for k in common_keys if attrs_a.get(k) == attrs_b.get(k))
    attr_score = matching_attrs / len(common_keys) if common_keys else 0

    combined = 0.4 * name_sim + 0.45 * attr_score + 0.15 * (1 if type_match else 0)
    combined += random.uniform(-0.1, 0.1)

    if combined > 0.55:
        return "match", min(0.95, combined)
    return "no_match", max(0.5, 1 - combined)


def load_json(path: Path) -> Any:
    """Load a JSON file."""
    with open(path) as f:
        return json.load(f)


def load_entities(data_dir: Path) -> Dict[str, Dict[str, Any]]:
    """Load entities as a lookup dict."""
    entities = load_json(data_dir / "entities.json")
    return {e["entity_id"]: e for e in entities}


def load_pairs(data_dir: Path) -> List[Dict[str, Any]]:
    """Load all pairs from all tiers."""
    all_pairs = []
    for tier in [1, 2, 3]:
        tier_path = data_dir / f"pairs_tier{tier}.json"
        if tier_path.exists():
            all_pairs.extend(load_json(tier_path))
    return all_pairs


def run_baseline(
    data_dir: Path,
    model: str = DEFAULT_MODEL,
    seed: int = 42,
    use_ollama: bool = True
) -> List[Dict[str, Any]]:
    """
    Run LLM baseline on all pairs.

    Args:
        data_dir: Path to data directory
        model: Ollama model to use
        seed: Random seed for simulation fallback
        use_ollama: Whether to attempt using Ollama

    Returns:
        List of prediction dicts
    """
    random.seed(seed)

    # Check Ollama availability
    ollama_available = use_ollama and check_ollama_available()
    model_available = ollama_available and check_model_available(model)

    if use_ollama and not ollama_available:
        print("Running LLM zero-shot baseline...")
        print(f"  WARNING: Ollama not available. Using simulated predictions.")
        print(f"  To use actual LLM: install Ollama and run 'ollama pull {model}'")
    elif use_ollama and not model_available:
        print("Running LLM zero-shot baseline...")
        print(f"  WARNING: Model '{model}' not found. Using simulated predictions.")
        print(f"  To use actual LLM: run 'ollama pull {model}'")
    elif ollama_available and model_available:
        print(f"Running LLM zero-shot baseline with Ollama ({model})...")
    else:
        print("Running LLM zero-shot baseline (simulated)...")

    entities = load_entities(data_dir)
    all_predictions = []

    for tier in [1, 2, 3]:
        tier_path = data_dir / f"pairs_tier{tier}.json"
        if not tier_path.exists():
            continue

        pairs = load_json(tier_path)
        print(f"  Processing Tier {tier} ({len(pairs)} pairs)...")

        for i, pair in enumerate(pairs):
            entity_a = entities.get(pair["entity_a"])
            entity_b = entities.get(pair["entity_b"])

            if entity_a is None or entity_b is None:
                all_predictions.append({
                    "pair_id": pair["pair_id"],
                    "predicted_label": "no_match",
                })
                continue

            # Use Ollama if available, otherwise simulate
            if model_available:
                prompt = get_pair_prompt(entity_a, entity_b)
                response = query_ollama(prompt, model)
                label, confidence = parse_llm_response(response)

                if i == 0:
                    print(f"    Sample response: {response[:100]}..." if response else "    No response")
            else:
                label, confidence = simulate_prediction(entity_a, entity_b, tier)

            all_predictions.append({
                "pair_id": pair["pair_id"],
                "predicted_label": label,
            })

            # Progress indicator
            if (i + 1) % 50 == 0:
                print(f"    Processed {i + 1}/{len(pairs)} pairs")

    # Print statistics
    match_count = sum(1 for p in all_predictions if p["predicted_label"] == "match")
    print(f"\n  Total pairs: {len(all_predictions)}")
    print(f"  Predicted matches: {match_count}")
    print(f"  Predicted no_match: {len(all_predictions) - match_count}")

    return all_predictions


def save_predictions(predictions: List[Dict[str, Any]], output_path: Path) -> None:
    """Save predictions to JSON file."""
    with open(output_path, "w") as f:
        json.dump(predictions, f, indent=2)
    print(f"Predictions saved to {output_path}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Run LLM zero-shot baseline on CrossER benchmark"
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).parent.parent / "data",
        help="Path to data directory"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent / "results" / "llm_zeroshot.json",
        help="Output path for predictions"
    )
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help=f"Ollama model to use (default: {DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--simulate",
        action="store_true",
        help="Force simulation mode (don't use Ollama)"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for simulation"
    )

    args = parser.parse_args()

    # Run baseline
    predictions = run_baseline(
        args.data_dir,
        model=args.model,
        seed=args.seed,
        use_ollama=not args.simulate
    )

    # Save results
    args.output.parent.mkdir(parents=True, exist_ok=True)
    save_predictions(predictions, args.output)

    print("\nBaseline complete!")


if __name__ == "__main__":
    main()

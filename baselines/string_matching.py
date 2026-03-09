"""
String matching baseline for CrossER benchmark.

Uses Jaro-Winkler similarity on entity names with a configurable threshold.
This baseline should perform poorly on CrossER due to adversarial pair design.
"""
import json
from pathlib import Path
from typing import Dict, List, Any, Tuple

try:
    import jellyfish
except ImportError:
    print("Warning: jellyfish not installed. Install with: pip install jellyfish")
    jellyfish = None


# Default threshold for match prediction
DEFAULT_THRESHOLD = 0.85


def jaro_winkler_similarity(s1: str, s2: str) -> float:
    """
    Compute Jaro-Winkler similarity between two strings.

    Returns a value between 0 and 1, where 1 means identical strings.
    """
    if jellyfish is None:
        # Fallback to simple implementation if jellyfish not available
        return simple_similarity(s1, s2)
    return jellyfish.jaro_winkler_similarity(s1, s2)


def simple_similarity(s1: str, s2: str) -> float:
    """
    Simple fallback similarity based on common characters.
    Not as good as Jaro-Winkler but works without dependencies.
    """
    s1 = s1.lower()
    s2 = s2.lower()

    if s1 == s2:
        return 1.0

    if len(s1) == 0 or len(s2) == 0:
        return 0.0

    # Compute character overlap
    set1 = set(s1)
    set2 = set(s2)
    intersection = len(set1 & set2)
    union = len(set1 | set2)

    jaccard = intersection / union if union > 0 else 0

    # Also consider length similarity
    len_sim = 1 - abs(len(s1) - len(s2)) / max(len(s1), len(s2))

    # Combine
    return 0.6 * jaccard + 0.4 * len_sim


def load_json(path: Path) -> Any:
    """Load a JSON file."""
    with open(path) as f:
        return json.load(f)


def load_entities(data_dir: Path) -> Dict[str, Dict[str, Any]]:
    """Load entities as a lookup dict."""
    entities = load_json(data_dir / "entities.json")
    return {e["entity_id"]: e for e in entities}


def load_pairs(data_dir: Path) -> List[Dict[str, Any]]:
    """Load all pairs."""
    # Try unified dataset first
    dataset_path = data_dir / "crosser_dataset.json"
    if dataset_path.exists():
        dataset = load_json(dataset_path)
        return dataset["pairs"]

    # Fall back to pairs.json
    pairs_path = data_dir / "pairs.json"
    if pairs_path.exists():
        return load_json(pairs_path)

    raise FileNotFoundError("No pairs file found")


def predict_pair(
    entity_a: Dict[str, Any],
    entity_b: Dict[str, Any],
    threshold: float = DEFAULT_THRESHOLD
) -> Tuple[str, float]:
    """
    Predict whether two entities match based on string similarity.

    Args:
        entity_a: First entity dict
        entity_b: Second entity dict
        threshold: Similarity threshold for match prediction

    Returns:
        Tuple of (predicted_label, similarity_score)
    """
    name_a = entity_a.get("name", "")
    name_b = entity_b.get("name", "")

    # Normalize names for comparison
    name_a_norm = name_a.lower().strip()
    name_b_norm = name_b.lower().strip()

    similarity = jaro_winkler_similarity(name_a_norm, name_b_norm)

    if similarity >= threshold:
        return "match", similarity
    else:
        return "no_match", similarity


def run_baseline(
    data_dir: Path,
    threshold: float = DEFAULT_THRESHOLD
) -> List[Dict[str, Any]]:
    """
    Run string matching baseline on all pairs.

    Args:
        data_dir: Path to data directory
        threshold: Similarity threshold for match prediction

    Returns:
        List of prediction dicts
    """
    print("Running string matching baseline...")
    print(f"  Threshold: {threshold}")

    entities = load_entities(data_dir)
    pairs = load_pairs(data_dir)

    predictions = []
    scores = []

    for pair in pairs:
        entity_a = entities.get(pair["entity_a"])
        entity_b = entities.get(pair["entity_b"])

        if entity_a is None or entity_b is None:
            print(f"  Warning: Missing entity for pair {pair['pair_id']}")
            predictions.append({
                "pair_id": pair["pair_id"],
                "predicted_label": "no_match",
            })
            continue

        label, score = predict_pair(entity_a, entity_b, threshold)
        predictions.append({
            "pair_id": pair["pair_id"],
            "predicted_label": label,
        })
        scores.append(score)

    # Print statistics
    match_count = sum(1 for p in predictions if p["predicted_label"] == "match")
    print(f"  Total pairs: {len(predictions)}")
    print(f"  Predicted matches: {match_count}")
    print(f"  Predicted no_match: {len(predictions) - match_count}")
    print(f"  Avg similarity: {sum(scores) / len(scores):.4f}" if scores else "")

    return predictions


def save_predictions(predictions: List[Dict[str, Any]], output_path: Path) -> None:
    """Save predictions to JSON file."""
    with open(output_path, "w") as f:
        json.dump(predictions, f, indent=2)
    print(f"Predictions saved to {output_path}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Run string matching baseline on CrossER benchmark"
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).parent.parent / "data",
        help="Path to data directory"
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD,
        help=f"Similarity threshold (default: {DEFAULT_THRESHOLD})"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent / "results" / "string_matching.json",
        help="Output path for predictions"
    )

    args = parser.parse_args()

    # Run baseline
    predictions = run_baseline(args.data_dir, args.threshold)

    # Save results
    args.output.parent.mkdir(parents=True, exist_ok=True)
    save_predictions(predictions, args.output)

    print("\nBaseline complete!")


if __name__ == "__main__":
    main()

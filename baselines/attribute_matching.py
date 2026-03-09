"""
Attribute matching baseline for CrossER benchmark.

Combines string similarity with attribute overlap for improved matching.
This baseline should perform better than pure string matching but still
struggle due to the adversarial pair design.

Scoring formula:
    score = (name_similarity * 0.3) + (attribute_overlap * 0.5) + (entity_type_match * 0.2)
"""
import json
from pathlib import Path
from typing import Dict, List, Any, Tuple, Set

try:
    import jellyfish
except ImportError:
    print("Warning: jellyfish not installed. Install with: pip install jellyfish")
    jellyfish = None


# Default threshold for match prediction
DEFAULT_THRESHOLD = 0.70

# Component weights
WEIGHTS = {
    "name_similarity": 0.3,
    "attribute_overlap": 0.5,
    "entity_type_match": 0.2,
}


def jaro_winkler_similarity(s1: str, s2: str) -> float:
    """Compute Jaro-Winkler similarity between two strings."""
    if jellyfish is None:
        return simple_similarity(s1, s2)
    return jellyfish.jaro_winkler_similarity(s1, s2)


def simple_similarity(s1: str, s2: str) -> float:
    """Simple fallback similarity based on common characters."""
    s1 = s1.lower()
    s2 = s2.lower()

    if s1 == s2:
        return 1.0
    if len(s1) == 0 or len(s2) == 0:
        return 0.0

    set1 = set(s1)
    set2 = set(s2)
    intersection = len(set1 & set2)
    union = len(set1 | set2)

    jaccard = intersection / union if union > 0 else 0
    len_sim = 1 - abs(len(s1) - len(s2)) / max(len(s1), len(s2))

    return 0.6 * jaccard + 0.4 * len_sim


def compute_attribute_overlap(
    attrs_a: Dict[str, Any],
    attrs_b: Dict[str, Any]
) -> float:
    """
    Compute attribute overlap between two attribute dictionaries.

    Uses Jaccard similarity on attribute key-value pairs, with fuzzy matching
    on string values.
    """
    if not attrs_a or not attrs_b:
        return 0.0

    # Get common keys
    keys_a = set(attrs_a.keys())
    keys_b = set(attrs_b.keys())
    common_keys = keys_a & keys_b

    if not common_keys:
        # No common keys, return low but non-zero score based on key overlap
        key_overlap = len(keys_a & keys_b) / len(keys_a | keys_b) if (keys_a | keys_b) else 0
        return key_overlap * 0.2

    # Compare values for common keys
    matching_values = 0
    total_compared = 0

    # Keys to skip (system-specific codes that won't match)
    skip_keys = {"internal_code", "vendor_code", "tax_code_id", "created_date"}

    for key in common_keys:
        if key in skip_keys:
            continue

        val_a = attrs_a[key]
        val_b = attrs_b[key]

        total_compared += 1

        if val_a == val_b:
            matching_values += 1
        elif isinstance(val_a, str) and isinstance(val_b, str):
            # Fuzzy match for strings
            sim = jaro_winkler_similarity(val_a.lower(), val_b.lower())
            if sim > 0.8:
                matching_values += sim

    if total_compared == 0:
        return 0.0

    return matching_values / total_compared


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
    threshold: float = DEFAULT_THRESHOLD,
    weights: Dict[str, float] = None
) -> Tuple[str, float, Dict[str, float]]:
    """
    Predict whether two entities match based on combined features.

    Args:
        entity_a: First entity dict
        entity_b: Second entity dict
        threshold: Overall score threshold for match prediction
        weights: Component weights (default: WEIGHTS)

    Returns:
        Tuple of (predicted_label, overall_score, component_scores)
    """
    if weights is None:
        weights = WEIGHTS

    # 1. Name similarity
    name_a = entity_a.get("name", "").lower().strip()
    name_b = entity_b.get("name", "").lower().strip()
    name_sim = jaro_winkler_similarity(name_a, name_b)

    # 2. Attribute overlap
    attrs_a = entity_a.get("attributes", {})
    attrs_b = entity_b.get("attributes", {})
    attr_overlap = compute_attribute_overlap(attrs_a, attrs_b)

    # 3. Entity type match
    type_a = entity_a.get("entity_type", "")
    type_b = entity_b.get("entity_type", "")
    type_match = 1.0 if type_a == type_b else 0.0

    # Compute weighted score
    overall_score = (
        weights["name_similarity"] * name_sim +
        weights["attribute_overlap"] * attr_overlap +
        weights["entity_type_match"] * type_match
    )

    component_scores = {
        "name_similarity": name_sim,
        "attribute_overlap": attr_overlap,
        "entity_type_match": type_match,
    }

    if overall_score >= threshold:
        return "match", overall_score, component_scores
    else:
        return "no_match", overall_score, component_scores


def run_baseline(
    data_dir: Path,
    threshold: float = DEFAULT_THRESHOLD,
    weights: Dict[str, float] = None
) -> List[Dict[str, Any]]:
    """
    Run attribute matching baseline on all pairs.

    Args:
        data_dir: Path to data directory
        threshold: Score threshold for match prediction
        weights: Component weights

    Returns:
        List of prediction dicts
    """
    print("Running attribute matching baseline...")
    print(f"  Threshold: {threshold}")
    print(f"  Weights: {weights or WEIGHTS}")

    entities = load_entities(data_dir)
    pairs = load_pairs(data_dir)

    predictions = []
    scores = []
    component_totals = {"name_similarity": 0, "attribute_overlap": 0, "entity_type_match": 0}

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

        label, score, components = predict_pair(entity_a, entity_b, threshold, weights)
        predictions.append({
            "pair_id": pair["pair_id"],
            "predicted_label": label,
        })
        scores.append(score)
        for k, v in components.items():
            component_totals[k] += v

    # Print statistics
    n = len(predictions)
    match_count = sum(1 for p in predictions if p["predicted_label"] == "match")
    print(f"  Total pairs: {n}")
    print(f"  Predicted matches: {match_count}")
    print(f"  Predicted no_match: {n - match_count}")

    if scores:
        print(f"  Avg overall score: {sum(scores) / len(scores):.4f}")
        print(f"  Avg name similarity: {component_totals['name_similarity'] / n:.4f}")
        print(f"  Avg attribute overlap: {component_totals['attribute_overlap'] / n:.4f}")
        print(f"  Avg type match: {component_totals['entity_type_match'] / n:.4f}")

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
        description="Run attribute matching baseline on CrossER benchmark"
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
        help=f"Score threshold (default: {DEFAULT_THRESHOLD})"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent / "results" / "attribute_matching.json",
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

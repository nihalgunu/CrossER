"""
Validate submission format for CrossER benchmark predictions.
"""
import json
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional


VALID_LABELS = {"match", "no_match", "ambiguous"}


def load_json(path: Path) -> Any:
    """Load a JSON file."""
    with open(path) as f:
        return json.load(f)


def check_prediction_structure(prediction: Any) -> Tuple[bool, Optional[str]]:
    """
    Check that a single prediction has the correct structure.

    Expected format:
    {
        "pair_id": "t1_001",
        "predicted_label": "match"
    }

    Args:
        prediction: A prediction dict

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(prediction, dict):
        return False, "Prediction must be a dict"

    if "pair_id" not in prediction:
        return False, "Prediction missing 'pair_id' field"

    if "predicted_label" not in prediction:
        return False, f"Prediction for {prediction.get('pair_id', 'unknown')} missing 'predicted_label' field"

    if not isinstance(prediction["pair_id"], str):
        return False, f"pair_id must be a string, got {type(prediction['pair_id'])}"

    if not isinstance(prediction["predicted_label"], str):
        return False, f"predicted_label must be a string, got {type(prediction['predicted_label'])}"

    if prediction["predicted_label"] not in VALID_LABELS:
        return False, f"Invalid label '{prediction['predicted_label']}'. Must be one of: {VALID_LABELS}"

    return True, None


def check_predictions_file(
    predictions_path: Path,
    ground_truth_pairs: List[Dict[str, Any]] = None
) -> Tuple[bool, List[str]]:
    """
    Validate a predictions file.

    Args:
        predictions_path: Path to predictions JSON file
        ground_truth_pairs: Optional list of ground truth pairs for completeness check

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    # Check file exists
    if not predictions_path.exists():
        return False, [f"File not found: {predictions_path}"]

    # Try to load JSON
    try:
        predictions = load_json(predictions_path)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"]

    # Check it's a list
    if not isinstance(predictions, list):
        return False, ["Predictions must be a list"]

    # Check each prediction
    seen_pair_ids = set()
    for i, pred in enumerate(predictions):
        is_valid, error = check_prediction_structure(pred)
        if not is_valid:
            errors.append(f"Prediction {i}: {error}")
            continue

        # Check for duplicates
        pair_id = pred["pair_id"]
        if pair_id in seen_pair_ids:
            errors.append(f"Duplicate pair_id: {pair_id}")
        seen_pair_ids.add(pair_id)

    # Check completeness if ground truth provided
    if ground_truth_pairs:
        gt_pair_ids = {p["pair_id"] for p in ground_truth_pairs}
        missing = gt_pair_ids - seen_pair_ids
        extra = seen_pair_ids - gt_pair_ids

        if missing:
            errors.append(f"Missing predictions for {len(missing)} pairs: {list(missing)[:5]}...")

        if extra:
            errors.append(f"Extra predictions for {len(extra)} unknown pairs: {list(extra)[:5]}...")

    return len(errors) == 0, errors


def validate_submission(
    predictions_path: Path,
    data_dir: Path
) -> Tuple[bool, Dict[str, Any]]:
    """
    Fully validate a submission.

    Args:
        predictions_path: Path to predictions JSON file
        data_dir: Path to data directory with ground truth files

    Returns:
        Tuple of (is_valid, validation_report)
    """
    report = {
        "file_path": str(predictions_path),
        "is_valid": False,
        "errors": [],
        "warnings": [],
        "statistics": {},
    }

    # Load ground truth
    all_pairs = []
    for tier in [1, 2, 3]:
        tier_path = data_dir / f"pairs_tier{tier}.json"
        if tier_path.exists():
            pairs = load_json(tier_path)
            all_pairs.extend(pairs)
        else:
            report["errors"].append(f"Ground truth file not found: {tier_path}")

    if report["errors"]:
        return False, report

    # Check predictions file
    is_valid, errors = check_predictions_file(predictions_path, all_pairs)
    report["errors"].extend(errors)

    if not is_valid:
        return False, report

    # Compute statistics
    predictions = load_json(predictions_path)
    pred_dict = {p["pair_id"]: p["predicted_label"] for p in predictions}

    label_counts = {}
    for label in pred_dict.values():
        label_counts[label] = label_counts.get(label, 0) + 1

    tier_counts = {"tier1": 0, "tier2": 0, "tier3": 0}
    for pair_id in pred_dict:
        if pair_id.startswith("t1_"):
            tier_counts["tier1"] += 1
        elif pair_id.startswith("t2_"):
            tier_counts["tier2"] += 1
        elif pair_id.startswith("t3_"):
            tier_counts["tier3"] += 1

    report["statistics"] = {
        "total_predictions": len(predictions),
        "label_distribution": label_counts,
        "predictions_per_tier": tier_counts,
    }

    # Add warnings for unusual distributions
    total = len(predictions)
    if total > 0:
        match_ratio = label_counts.get("match", 0) / total
        if match_ratio < 0.2 or match_ratio > 0.8:
            report["warnings"].append(
                f"Unusual match ratio ({match_ratio:.2%}). Expected around 50%."
            )

    report["is_valid"] = True
    return True, report


def main():
    """Command-line interface for format checking."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate CrossER benchmark submission format"
    )
    parser.add_argument(
        "predictions_file",
        type=Path,
        help="Path to predictions JSON file"
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).parent.parent / "data",
        help="Path to data directory"
    )

    args = parser.parse_args()

    is_valid, report = validate_submission(args.predictions_file, args.data_dir)

    print("\n" + "=" * 60)
    print("CrossER Submission Validation Report")
    print("=" * 60)

    print(f"\nFile: {report['file_path']}")
    print(f"Valid: {'YES' if report['is_valid'] else 'NO'}")

    if report["errors"]:
        print(f"\nErrors ({len(report['errors'])}):")
        for error in report["errors"]:
            print(f"  - {error}")

    if report["warnings"]:
        print(f"\nWarnings ({len(report['warnings'])}):")
        for warning in report["warnings"]:
            print(f"  - {warning}")

    if report["statistics"]:
        print("\nStatistics:")
        stats = report["statistics"]
        print(f"  Total predictions: {stats['total_predictions']}")
        print(f"  Label distribution: {stats['label_distribution']}")
        print(f"  Per-tier: {stats['predictions_per_tier']}")

    print("\n" + "=" * 60)

    return 0 if is_valid else 1


if __name__ == "__main__":
    exit(main())

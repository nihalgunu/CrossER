#!/usr/bin/env python3
"""
Run all baselines for CrossER benchmark and generate evaluation results.

Baselines are organized along two axes:
  Axis 1 (Knowledge Gap): no_context vs with_context
  Axis 2 (Context Mechanism): full_dump vs RAG vs other approaches

Usage:
    python run_baselines.py [--data-dir DATA_DIR] [--include-llm]
"""
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "eval"))

from string_matching import run_baseline as run_string_matching
from attribute_matching import run_baseline as run_attribute_matching


def load_json(path: Path):
    """Load a JSON file."""
    with open(path) as f:
        return json.load(f)


def save_json(data, path: Path):
    """Save data to JSON file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def load_pairs(data_dir: Path):
    """Load all pairs."""
    dataset_path = data_dir / "crosser_dataset.json"
    if dataset_path.exists():
        dataset = load_json(dataset_path)
        return dataset["pairs"]

    pairs_path = data_dir / "pairs.json"
    if pairs_path.exists():
        return load_json(pairs_path)

    raise FileNotFoundError("No pairs file found")


def evaluate_predictions(predictions, ground_truth):
    """
    Evaluate predictions against ground truth.

    Returns metrics dict with precision, recall, F1 overall and per-label.
    """
    pred_lookup = {p["pair_id"]: p["predicted_label"] for p in predictions}

    # Overall binary metrics (match as positive class)
    tp = fp = fn = tn = 0
    for pair in ground_truth:
        gt_label = pair["label"]
        pred_label = pred_lookup.get(pair["pair_id"], "no_match")

        # Skip ambiguous for binary evaluation
        if gt_label == "ambiguous":
            continue

        if gt_label == "match" and pred_label == "match":
            tp += 1
        elif gt_label != "match" and pred_label == "match":
            fp += 1
        elif gt_label == "match" and pred_label != "match":
            fn += 1
        else:
            tn += 1

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else 0

    # Per-label metrics
    per_label = {}
    for target_label in ["match", "no_match"]:
        label_tp = label_fp = label_fn = 0
        for pair in ground_truth:
            gt = pair["label"]
            pred = pred_lookup.get(pair["pair_id"], "no_match")

            if gt == target_label and pred == target_label:
                label_tp += 1
            elif gt != target_label and pred == target_label:
                label_fp += 1
            elif gt == target_label and pred != target_label:
                label_fn += 1

        label_prec = label_tp / (label_tp + label_fp) if (label_tp + label_fp) > 0 else 0
        label_rec = label_tp / (label_tp + label_fn) if (label_tp + label_fn) > 0 else 0
        label_f1 = 2 * label_prec * label_rec / (label_prec + label_rec) if (label_prec + label_rec) > 0 else 0

        per_label[target_label] = {
            "precision": round(label_prec, 4),
            "recall": round(label_rec, 4),
            "f1": round(label_f1, 4),
        }

    return {
        "overall": {
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
            "accuracy": round(accuracy, 4),
        },
        "per_label": per_label,
        "confusion": {"tp": tp, "fp": fp, "fn": fn, "tn": tn},
    }


def run_all_baselines(data_dir: Path, results_dir: Path):
    """Run all baselines and evaluate them."""
    print("=" * 70)
    print("CrossER Baseline Evaluation")
    print("=" * 70)

    # Load ground truth
    all_gt = load_pairs(data_dir)

    if not all_gt:
        print("Error: No ground truth pairs found. Generate data first.")
        return None

    # Filter to test split for evaluation
    test_pairs = [p for p in all_gt if p.get("split") == "test"]
    if not test_pairs:
        test_pairs = all_gt  # Use all if no split field

    print(f"\nLoaded {len(all_gt)} total pairs")
    print(f"Evaluating on {len(test_pairs)} test pairs")

    results_dir.mkdir(parents=True, exist_ok=True)
    all_results = {}

    # Run string matching baseline
    print("\n" + "-" * 70)
    predictions = run_string_matching(data_dir)
    save_json(predictions, results_dir / "string_matching.json")

    # Filter predictions to test set
    test_pair_ids = {p["pair_id"] for p in test_pairs}
    test_predictions = [p for p in predictions if p["pair_id"] in test_pair_ids]

    metrics = evaluate_predictions(test_predictions, test_pairs)
    all_results["string_matching"] = metrics
    print(f"  Results: P={metrics['overall']['precision']:.3f}, R={metrics['overall']['recall']:.3f}, F1={metrics['overall']['f1']:.3f}")

    # Run attribute matching baseline
    print("\n" + "-" * 70)
    predictions = run_attribute_matching(data_dir)
    save_json(predictions, results_dir / "attribute_matching.json")

    test_predictions = [p for p in predictions if p["pair_id"] in test_pair_ids]
    metrics = evaluate_predictions(test_predictions, test_pairs)
    all_results["attribute_matching"] = metrics
    print(f"  Results: P={metrics['overall']['precision']:.3f}, R={metrics['overall']['recall']:.3f}, F1={metrics['overall']['f1']:.3f}")

    # Print summary table
    print("\n" + "=" * 70)
    print("BASELINE RESULTS SUMMARY (Test Set)")
    print("=" * 70)
    print(f"\n{'Method':<25} {'Precision':>12} {'Recall':>12} {'F1':>12} {'Accuracy':>12}")
    print("-" * 75)

    for method, metrics in all_results.items():
        print(
            f"{method:<25} "
            f"{metrics['overall']['precision']:>12.4f} "
            f"{metrics['overall']['recall']:>12.4f} "
            f"{metrics['overall']['f1']:>12.4f} "
            f"{metrics['overall']['accuracy']:>12.4f}"
        )

    print("-" * 75)

    # Save summary
    save_json(all_results, results_dir / "summary.json")
    print(f"\nResults saved to {results_dir}")

    return all_results


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Run all CrossER baselines and evaluate"
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).parent.parent / "data",
        help="Path to data directory"
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path(__file__).parent / "results",
        help="Path to results directory"
    )

    args = parser.parse_args()

    results = run_all_baselines(args.data_dir, args.results_dir)

    if results is None:
        return 1

    return 0


if __name__ == "__main__":
    exit(main())

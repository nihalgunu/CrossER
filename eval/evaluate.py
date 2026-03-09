#!/usr/bin/env python3
"""
Main evaluation script for CrossER benchmark.

Computes precision, recall, F1 for overall and per-label metrics.

Usage:
    python evaluate.py predictions.json [--data-dir DATA_DIR] [--output OUTPUT]
"""
import argparse
import json
from pathlib import Path
from typing import Dict, List, Any, Optional

from metrics import (
    compute_metrics,
    compute_per_label_metrics,
)
from format_checker import validate_submission


def load_json(path: Path) -> Any:
    """Load a JSON file."""
    with open(path) as f:
        return json.load(f)


def load_ground_truth(data_dir: Path) -> List[Dict[str, Any]]:
    """Load ground truth pairs."""
    # Try unified dataset first
    dataset_path = data_dir / "crosser_dataset.json"
    if dataset_path.exists():
        dataset = load_json(dataset_path)
        return dataset["pairs"]

    # Fall back to pairs.json
    pairs_path = data_dir / "pairs.json"
    if pairs_path.exists():
        return load_json(pairs_path)

    raise FileNotFoundError("No pairs file found (crosser_dataset.json or pairs.json)")


def load_predictions(predictions_path: Path) -> Dict[str, str]:
    """Load predictions as a dict mapping pair_id to predicted_label."""
    predictions = load_json(predictions_path)
    return {p["pair_id"]: p["predicted_label"] for p in predictions}


def evaluate(
    predictions_path: Path,
    data_dir: Path,
    split: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Run full evaluation on a predictions file.

    Args:
        predictions_path: Path to predictions JSON file
        data_dir: Path to data directory
        split: Optional split to evaluate on (train, val, test, or None for all)

    Returns:
        Dict with all evaluation results
    """
    # Validate submission first
    is_valid, report = validate_submission(predictions_path, data_dir)
    if not is_valid:
        return {
            "success": False,
            "errors": report["errors"],
        }

    # Load data
    all_pairs = load_ground_truth(data_dir)
    predictions = load_predictions(predictions_path)

    # Filter by split if specified
    if split:
        pairs = [p for p in all_pairs if p.get("split") == split]
    else:
        pairs = all_pairs

    results = {
        "success": True,
        "predictions_file": str(predictions_path),
        "split": split or "all",
        "total_pairs": len(pairs),
    }

    # Compute overall metrics
    overall = compute_metrics(pairs, predictions)
    results["overall"] = {
        "precision": round(overall["precision"], 4),
        "recall": round(overall["recall"], 4),
        "f1": round(overall["f1"], 4),
        "accuracy": round(overall["accuracy"], 4),
        "evaluated_pairs": overall["evaluated_pairs"],
    }

    # Compute per-label metrics
    per_label = compute_per_label_metrics(pairs, predictions)
    results["per_label"] = {}
    for label, metrics in per_label.items():
        results["per_label"][label] = {
            "precision": round(metrics["precision"], 4),
            "recall": round(metrics["recall"], 4),
            "f1": round(metrics["f1"], 4),
            "support": metrics["support"],
            "predicted": metrics["predicted"],
        }

    # Compute metrics by knowledge requirement
    knowledge_pairs = [p for p in pairs if p.get("requires_knowledge")]
    if knowledge_pairs:
        knowledge_metrics = compute_metrics(knowledge_pairs, predictions)
        results["knowledge_required"] = {
            "precision": round(knowledge_metrics["precision"], 4),
            "recall": round(knowledge_metrics["recall"], 4),
            "f1": round(knowledge_metrics["f1"], 4),
            "pairs": len(knowledge_pairs),
        }

    return results


def print_results(results: Dict[str, Any]) -> None:
    """Pretty-print evaluation results."""
    if not results["success"]:
        print("\nEvaluation failed!")
        print("Errors:")
        for error in results.get("errors", []):
            print(f"  - {error}")
        return

    print("\n" + "=" * 70)
    print("CrossER Benchmark Evaluation Results")
    print("=" * 70)
    print(f"\nPredictions: {results['predictions_file']}")
    print(f"Split: {results['split']}")
    print(f"Total pairs: {results['total_pairs']}")

    # Overall results
    print("\n" + "-" * 70)
    print("Overall Results")
    print("-" * 70)
    overall = results["overall"]
    print(f"Precision:  {overall['precision']:.4f}")
    print(f"Recall:     {overall['recall']:.4f}")
    print(f"F1:         {overall['f1']:.4f}")
    print(f"Accuracy:   {overall['accuracy']:.4f}")
    print(f"Evaluated:  {overall['evaluated_pairs']}")

    # Per-label results
    print("\n" + "-" * 70)
    print("Per-Label Results")
    print("-" * 70)

    header = f"{'Label':<12} {'Precision':>10} {'Recall':>10} {'F1':>10} {'Support':>10} {'Predicted':>10}"
    print(header)
    print("-" * len(header))

    for label in ["match", "no_match", "ambiguous"]:
        if label in results["per_label"]:
            m = results["per_label"][label]
            print(
                f"{label:<12} "
                f"{m['precision']:>10.4f} "
                f"{m['recall']:>10.4f} "
                f"{m['f1']:>10.4f} "
                f"{m['support']:>10d} "
                f"{m['predicted']:>10d}"
            )

    # Knowledge-required results (if available)
    if "knowledge_required" in results:
        print("\n" + "-" * 70)
        print("Knowledge-Required Pairs (subset)")
        print("-" * 70)
        kr = results["knowledge_required"]
        print(f"Precision:  {kr['precision']:.4f}")
        print(f"Recall:     {kr['recall']:.4f}")
        print(f"F1:         {kr['f1']:.4f}")
        print(f"Pairs:      {kr['pairs']}")

    print("\n" + "=" * 70)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Evaluate predictions on the CrossER benchmark"
    )
    parser.add_argument(
        "predictions",
        type=Path,
        help="Path to predictions JSON file"
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).parent.parent / "data",
        help="Path to data directory (default: ../data)"
    )
    parser.add_argument(
        "--split",
        type=str,
        choices=["train", "val", "test"],
        default=None,
        help="Evaluate on specific split only"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional path to save results JSON"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only output JSON, no pretty-printing"
    )

    args = parser.parse_args()

    # Run evaluation
    results = evaluate(args.predictions, args.data_dir, args.split)

    # Print results
    if not args.quiet:
        print_results(results)

    # Save results if requested
    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        if not args.quiet:
            print(f"\nResults saved to {args.output}")

    # Return appropriate exit code
    if results["success"]:
        return 0
    else:
        return 1


if __name__ == "__main__":
    exit(main())

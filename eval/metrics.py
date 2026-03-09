"""
Metric computation helpers for CrossER benchmark evaluation.
"""
from typing import Dict, List, Any, Tuple
from collections import Counter


def compute_precision(tp: int, fp: int) -> float:
    """Compute precision from true positives and false positives."""
    if tp + fp == 0:
        return 0.0
    return tp / (tp + fp)


def compute_recall(tp: int, fn: int) -> float:
    """Compute recall from true positives and false negatives."""
    if tp + fn == 0:
        return 0.0
    return tp / (tp + fn)


def compute_f1(precision: float, recall: float) -> float:
    """Compute F1 score from precision and recall."""
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)


def compute_accuracy(correct: int, total: int) -> float:
    """Compute accuracy from correct predictions and total count."""
    if total == 0:
        return 0.0
    return correct / total


def compute_confusion_matrix(
    ground_truth: List[str],
    predictions: List[str],
    labels: List[str] = None
) -> Dict[str, Dict[str, int]]:
    """
    Compute confusion matrix for multi-class classification.

    Args:
        ground_truth: List of ground truth labels
        predictions: List of predicted labels
        labels: List of label names (optional, inferred if not provided)

    Returns:
        Nested dict where matrix[actual][predicted] = count
    """
    if labels is None:
        labels = sorted(set(ground_truth) | set(predictions))

    matrix = {actual: {pred: 0 for pred in labels} for actual in labels}

    for gt, pred in zip(ground_truth, predictions):
        if gt in matrix and pred in matrix[gt]:
            matrix[gt][pred] += 1

    return matrix


def compute_binary_metrics(
    ground_truth: List[str],
    predictions: List[str],
    positive_label: str = "match"
) -> Dict[str, float]:
    """
    Compute binary classification metrics.

    Args:
        ground_truth: List of ground truth labels
        predictions: List of predicted labels
        positive_label: The label considered "positive"

    Returns:
        Dict with precision, recall, f1, accuracy
    """
    tp = fp = fn = tn = 0

    for gt, pred in zip(ground_truth, predictions):
        if gt == positive_label and pred == positive_label:
            tp += 1
        elif gt != positive_label and pred == positive_label:
            fp += 1
        elif gt == positive_label and pred != positive_label:
            fn += 1
        else:
            tn += 1

    precision = compute_precision(tp, fp)
    recall = compute_recall(tp, fn)
    f1 = compute_f1(precision, recall)
    accuracy = compute_accuracy(tp + tn, tp + fp + fn + tn)

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "accuracy": accuracy,
        "true_positives": tp,
        "false_positives": fp,
        "false_negatives": fn,
        "true_negatives": tn,
    }


def compute_macro_f1(
    ground_truth: List[str],
    predictions: List[str],
    labels: List[str] = None
) -> float:
    """
    Compute macro-averaged F1 score across all labels.

    Args:
        ground_truth: List of ground truth labels
        predictions: List of predicted labels
        labels: List of label names

    Returns:
        Macro F1 score
    """
    if labels is None:
        labels = sorted(set(ground_truth) | set(predictions))

    f1_scores = []
    for label in labels:
        metrics = compute_binary_metrics(ground_truth, predictions, label)
        f1_scores.append(metrics["f1"])

    return sum(f1_scores) / len(f1_scores) if f1_scores else 0.0


def compute_weighted_f1(
    ground_truth: List[str],
    predictions: List[str],
    labels: List[str] = None
) -> float:
    """
    Compute weighted F1 score (weighted by label frequency).

    Args:
        ground_truth: List of ground truth labels
        predictions: List of predicted labels
        labels: List of label names

    Returns:
        Weighted F1 score
    """
    if labels is None:
        labels = sorted(set(ground_truth) | set(predictions))

    label_counts = Counter(ground_truth)
    total = len(ground_truth)

    weighted_f1 = 0.0
    for label in labels:
        metrics = compute_binary_metrics(ground_truth, predictions, label)
        weight = label_counts.get(label, 0) / total if total > 0 else 0
        weighted_f1 += metrics["f1"] * weight

    return weighted_f1


def compute_tier_metrics(
    pairs: List[Dict[str, Any]],
    predictions: Dict[str, str],
    include_ambiguous: bool = False
) -> Dict[str, Any]:
    """
    Compute metrics for a specific tier of pairs.

    Args:
        pairs: List of ground truth pair dicts
        predictions: Dict mapping pair_id to predicted_label
        include_ambiguous: Whether to include ambiguous pairs in evaluation

    Returns:
        Dict with all metrics for this tier
    """
    ground_truth = []
    preds = []

    for pair in pairs:
        pair_id = pair["pair_id"]
        gt_label = pair["label"]

        # Skip ambiguous if not including
        if not include_ambiguous and gt_label == "ambiguous":
            continue

        if pair_id in predictions:
            ground_truth.append(gt_label)
            preds.append(predictions[pair_id])

    if not ground_truth:
        return {
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "accuracy": 0.0,
            "total_pairs": 0,
            "evaluated_pairs": 0,
        }

    # Compute binary metrics treating "match" as positive class
    binary_metrics = compute_binary_metrics(ground_truth, preds, "match")

    # Compute confusion matrix
    confusion = compute_confusion_matrix(
        ground_truth, preds,
        labels=["match", "no_match", "ambiguous"] if include_ambiguous else ["match", "no_match"]
    )

    return {
        **binary_metrics,
        "total_pairs": len(pairs),
        "evaluated_pairs": len(ground_truth),
        "confusion_matrix": confusion,
    }


def compute_overall_metrics(
    tier_metrics: Dict[str, Dict[str, Any]]
) -> Dict[str, float]:
    """
    Compute overall metrics across all tiers.

    Args:
        tier_metrics: Dict mapping tier name to metrics dict

    Returns:
        Dict with overall precision, recall, f1, accuracy
    """
    total_tp = sum(m.get("true_positives", 0) for m in tier_metrics.values())
    total_fp = sum(m.get("false_positives", 0) for m in tier_metrics.values())
    total_fn = sum(m.get("false_negatives", 0) for m in tier_metrics.values())
    total_tn = sum(m.get("true_negatives", 0) for m in tier_metrics.values())

    precision = compute_precision(total_tp, total_fp)
    recall = compute_recall(total_tp, total_fn)
    f1 = compute_f1(precision, recall)
    accuracy = compute_accuracy(
        total_tp + total_tn,
        total_tp + total_fp + total_fn + total_tn
    )

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "accuracy": accuracy,
        "total_evaluated": total_tp + total_fp + total_fn + total_tn,
    }


def format_confusion_matrix(
    matrix: Dict[str, Dict[str, int]],
    labels: List[str] = None
) -> str:
    """
    Format confusion matrix as a readable string.

    Args:
        matrix: Confusion matrix dict
        labels: Order of labels (optional)

    Returns:
        Formatted string representation
    """
    if labels is None:
        labels = sorted(matrix.keys())

    # Header
    col_width = max(len(label) for label in labels) + 2
    header = " " * col_width + "".join(f"{label:>{col_width}}" for label in labels)
    lines = [header, "-" * len(header)]

    # Rows
    for actual in labels:
        row = f"{actual:>{col_width}}"
        for pred in labels:
            count = matrix.get(actual, {}).get(pred, 0)
            row += f"{count:>{col_width}}"
        lines.append(row)

    return "\n".join(lines)


def compute_metrics(
    pairs: List[Dict[str, Any]],
    predictions: Dict[str, str],
) -> Dict[str, Any]:
    """
    Compute overall metrics for a set of pairs.

    Args:
        pairs: List of ground truth pair dicts
        predictions: Dict mapping pair_id to predicted_label

    Returns:
        Dict with precision, recall, f1, accuracy
    """
    ground_truth = []
    preds = []

    for pair in pairs:
        pair_id = pair["pair_id"]
        gt_label = pair["label"]

        if pair_id in predictions:
            ground_truth.append(gt_label)
            preds.append(predictions[pair_id])

    if not ground_truth:
        return {
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "accuracy": 0.0,
            "evaluated_pairs": 0,
        }

    # For entity resolution, we treat "match" as positive class
    binary_metrics = compute_binary_metrics(ground_truth, preds, "match")

    return {
        "precision": binary_metrics["precision"],
        "recall": binary_metrics["recall"],
        "f1": binary_metrics["f1"],
        "accuracy": binary_metrics["accuracy"],
        "evaluated_pairs": len(ground_truth),
        "true_positives": binary_metrics["true_positives"],
        "false_positives": binary_metrics["false_positives"],
        "false_negatives": binary_metrics["false_negatives"],
        "true_negatives": binary_metrics["true_negatives"],
    }


def compute_per_label_metrics(
    pairs: List[Dict[str, Any]],
    predictions: Dict[str, str],
) -> Dict[str, Dict[str, Any]]:
    """
    Compute metrics per label (match, no_match, ambiguous).

    Args:
        pairs: List of ground truth pair dicts
        predictions: Dict mapping pair_id to predicted_label

    Returns:
        Dict mapping label to metrics
    """
    results = {}
    labels = ["match", "no_match", "ambiguous"]

    for target_label in labels:
        # Get pairs with this label
        label_pairs = [p for p in pairs if p["label"] == target_label]
        if not label_pairs:
            continue

        # Count predictions
        tp = fp = fn = 0
        support = len(label_pairs)
        predicted = 0

        for pair in pairs:
            pair_id = pair["pair_id"]
            gt = pair["label"]
            pred = predictions.get(pair_id)

            if pred is None:
                continue

            if pred == target_label:
                predicted += 1

            if gt == target_label:
                if pred == target_label:
                    tp += 1
                else:
                    fn += 1
            else:
                if pred == target_label:
                    fp += 1

        precision = compute_precision(tp, fp)
        recall = compute_recall(tp, fn)
        f1 = compute_f1(precision, recall)

        results[target_label] = {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "support": support,
            "predicted": predicted,
        }

    return results


def compute_knowledge_delta(
    closed_metrics: Dict[str, Any],
    open_metrics: Dict[str, Any]
) -> Dict[str, float]:
    """
    Compute the delta between closed-book and open-book performance.

    This is a key metric for CrossER - it measures how much institutional
    knowledge improves entity resolution performance.

    Args:
        closed_metrics: Metrics without access to rules/decisions
        open_metrics: Metrics with access to rules/decisions

    Returns:
        Dict with delta metrics
    """
    return {
        "precision_delta": open_metrics.get("precision", 0) - closed_metrics.get("precision", 0),
        "recall_delta": open_metrics.get("recall", 0) - closed_metrics.get("recall", 0),
        "f1_delta": open_metrics.get("f1", 0) - closed_metrics.get("f1", 0),
        "accuracy_delta": open_metrics.get("accuracy", 0) - closed_metrics.get("accuracy", 0),
    }

#!/usr/bin/env python3
"""
Example: Test your own context retrieval mechanism on CrossER.

This shows how to plug in a custom context approach and evaluate it.

Usage:
    python example_custom_context.py --provider anthropic
    python example_custom_context.py --provider openai --model gpt-4o
"""
import json
from pathlib import Path
from typing import Dict, Any

from llm_baseline import (
    ContextMechanism,
    LLMProvider,
    AnthropicProvider,
    OpenAIProvider,
    run_llm_baseline,
)


# =============================================================================
# STEP 1: Implement your context retrieval mechanism
# =============================================================================

class MyCustomContext(ContextMechanism):
    """
    Your custom context retrieval implementation.

    Given an entity pair and the full context store, return relevant
    context as a string to include in the LLM prompt.
    """

    def __init__(self, top_k: int = 10):
        self.top_k = top_k

    @property
    def name(self) -> str:
        return "my_custom_context"

    def get_context(
        self,
        entity_a: Dict[str, Any],
        entity_b: Dict[str, Any],
        full_context: Dict[str, Any]
    ) -> str:
        """
        Return context string for the entity pair.

        Args:
            entity_a: First entity dict with keys:
                - entity_id: str
                - source_system: str (ERP_ALPHA, ERP_BETA, etc.)
                - entity_type: str (product, supplier, etc.)
                - name: str
                - attributes: dict

            entity_b: Second entity dict (same structure)

            full_context: Dict containing:
                - migration_records: List[Dict] - system-to-system mappings
                - alias_table: List[Dict] - known alternative names
                - code_mappings: List[Dict] - legacy code translations
                - system_crosswalks: List[Dict] - multi-hop mappings
                - transaction_logs: List[Dict] - historical references
                - data_quality_flags: List[Dict] - review notes
                - business_rules: List[Dict] - domain rules
                - rules: List[Dict] - classification rules

        Returns:
            String to append to LLM prompt as context.
            Return "" for no context.
        """

        # ---------------------------------------------------------------------
        # YOUR IMPLEMENTATION HERE
        # ---------------------------------------------------------------------
        #
        # Example: Simple keyword matching on entity names
        # Replace this with your RAG system, embedding search, etc.

        relevant = []
        name_a = entity_a["name"].lower()
        name_b = entity_b["name"].lower()

        # Search migration records for name matches
        for record in full_context.get("migration_records", []):
            source = record.get("source_code", "").lower()
            target = record.get("target_code", "").lower()

            # Check if either entity name appears in the record
            if (name_a in source or name_a in target or
                name_b in source or name_b in target):
                relevant.append(
                    f"MIGRATION: {record['source_code']} -> {record['target_code']}"
                )

        # Search alias table
        for alias in full_context.get("alias_table", []):
            primary = alias.get("primary_name", "").lower()
            alias_name = alias.get("alias_name", "").lower()

            if (name_a in primary or name_a in alias_name or
                name_b in primary or name_b in alias_name):
                relevant.append(
                    f"ALIAS: {alias['primary_name']} = {alias['alias_name']}"
                )

        # Search code mappings
        for mapping in full_context.get("code_mappings", []):
            legacy = mapping.get("legacy_code", "").lower()
            standard = mapping.get("standard_name", "").lower()

            if (name_a in legacy or name_a in standard or
                name_b in legacy or name_b in standard):
                relevant.append(
                    f"CODE: {mapping['legacy_code']} -> {mapping['standard_name']}"
                )

        # Return top-k results
        if not relevant:
            return ""

        return "RETRIEVED CONTEXT:\n" + "\n".join(relevant[:self.top_k])


# =============================================================================
# STEP 2: Run evaluation
# =============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Test custom context on CrossER")
    parser.add_argument("--data-dir", type=Path,
                        default=Path(__file__).parent.parent / "data")
    parser.add_argument("--provider", choices=["openai", "anthropic"],
                        default="anthropic")
    parser.add_argument("--model", type=str, default=None)
    parser.add_argument("--limit", type=int, default=50,
                        help="Number of test pairs to evaluate (default: 50)")
    parser.add_argument("--top-k", type=int, default=10,
                        help="Top-k context items to retrieve")

    args = parser.parse_args()

    # Initialize LLM provider
    if args.provider == "openai":
        model = args.model or "gpt-4o"
        provider = OpenAIProvider(model=model)
    else:
        model = args.model or "claude-sonnet-4-20250514"
        provider = AnthropicProvider(model=model)

    # Initialize your custom context mechanism
    mechanism = MyCustomContext(top_k=args.top_k)

    print(f"Testing {mechanism.name} with {args.provider}/{model}")
    print(f"Evaluating on {args.limit} test pairs...")

    # Run evaluation
    predictions = run_llm_baseline(
        args.data_dir,
        provider,
        mechanism,
        split="test",
        limit=args.limit
    )

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

    print(f"\n{'='*50}")
    print(f"Results for {mechanism.name}:")
    print(f"  Precision: {precision:.3f}")
    print(f"  Recall:    {recall:.3f}")
    print(f"  F1:        {f1:.3f}")
    print(f"{'='*50}")

    # Save predictions
    output_path = Path(__file__).parent / "results" / f"{mechanism.name}_results.json"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        json.dump({
            "mechanism": mechanism.name,
            "provider": args.provider,
            "model": model,
            "metrics": {"precision": precision, "recall": recall, "f1": f1},
            "predictions": predictions
        }, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()

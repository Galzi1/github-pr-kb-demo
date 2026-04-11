---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/10
pr_title: "feat: add minimum charge helper for final demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/10#discussion_r3067728955
author: "Galzi1"
date: 2026-04-11T07:13:25+00:00
category: domain_knowledge
confidence: 0.92
needs_review: false
comment_id: 3067728955
---

# Clarifying whether minimum_charge applies to pre-tax subtotal or final customer-facing total impacts pricing policy and invoicing behavior.

## Context

A minimum charge helper has been added to support the final demo. This feature establishes a floor value for charges, but the exact scope of this floor requires clarification in the implementation documentation.

## Key Insight

The minimum_charge parameter requires explicit specification regarding its application point in the pricing calculation flow. It must be clearly documented whether minimum_charge represents a floor applied to the pre-tax subtotal or a floor applied to the final amount presented to customers after all taxes and adjustments are calculated.

## Implications

Not stated in the source comment.

```
@@ -52,3 +52,15 @@ def calculate_total_with_capped_percentage_discount(
     discount_amount = min(subtotal * discount_rate, max_discount_amount)
     discounted_subtotal = subtotal - discount_amount
     return calculate_total(discounted_subtotal, sales_tax_rate=sales_tax_rate)
+
+
+def calculate_total_with_minimum_charge(
+    subtotal: float,
+    sales_tax_rate: float,
+    discount_amount: float,
+    minimum_charge: float = 0.0,
+) -> float:
+    """Apply a discount before tax, but never reduce the subtotal below a floor."""
```

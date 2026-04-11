---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/10
pr_title: "feat: add minimum charge helper for final demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/10#discussion_r3067728949
author: "Galzi1"
date: 2026-04-11T07:13:24+00:00
category: architecture_decision
confidence: 0.92
needs_review: false
comment_id: 3067728949
---

# Consolidating discount logic into a single helper reduces duplication and ensures pricing rules are maintained in one place.

## Context

A minimum charge helper is being introduced for the final demonstration. The existing codebase contains discount helper functionality that manages discount clamping rules.

## Decision

The minimum charge helper should normalize the floored subtotal and then reuse the existing discount helper rather than implementing independent pricing calculation logic. This approach consolidates responsibility for discount clamping rules into a single helper, avoiding duplication of pricing mathematics across multiple helpers.

## Consequences

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
+
+    adjusted_subtotal = max(subtotal - discount_amount, minimum_charge)
+    return calculate_total(adjusted_subtotal, sales_tax_rate=sales_tax_rate)
```

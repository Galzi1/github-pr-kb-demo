---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/10
pr_title: "feat: add minimum charge helper for final demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/10#discussion_r3067729934
author: "qodo-code-review[bot]"
date: 2026-04-11T07:14:43+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 3067729934
---

# Negative discount or minimum_charge inputs silently produce incorrect financial calculations, contradicting the validation behavior of similar functions in the same module.

## Symptom

The `calculate_total_with_minimum_charge` function accepts negative values for `discount_amount` and `minimum_charge` parameters without validation. Negative discount amounts cause the function to increase the subtotal instead of decreasing it, resulting in overcharges. Negative minimum charge values can produce invalid negative totals.

## Root Cause

Input validation is missing from the `calculate_total_with_minimum_charge` function. This creates an inconsistency with the existing `calculate_total_with_discount` function, which already rejects negative discounts. The absence of guards allows invalid parameters to silently produce incorrect financial calculations.

## Fix or Workaround

Add input validation to reject negative values for both parameters. Implement guards that raise a `ValueError` when `discount_amount` is negative and when `minimum_charge` is negative. This approach aligns the new helper function with the validation contract already established by `calculate_total_with_discount`. Consider also validating that `subtotal` is non-negative if the module assumes non-negative subtotals elsewhere.

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

---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3
pr_title: "feat: add percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3#discussion_r3066877543
author: "qodo-code-review[bot]"
date: 2026-04-10T21:43:26+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 3066877543
---

# Unbounded discount_rate parameter can produce negative totals or unintended surcharges due to missing input validation, unlike the similar absolute discount function that includes guards.

## Symptom

The `calculate_total_with_percentage_discount` function can produce unexpected results when given invalid discount rates. Specifically, if the discount rate exceeds 1.0, the function returns a negative total. If the discount rate is negative, the function increases the subtotal instead of applying a discount, contrary to the function's intended behavior.

## Root Cause

The function performs the calculation `subtotal * (1 - discount_rate)` without validating the `discount_rate` parameter. This allows out-of-range values to produce mathematically valid but logically incorrect results. The function lacks the input validation and safeguards present in the existing absolute discount helper function, which rejects negative discounts and ensures the result never falls below zero.

## Fix or Workaround

Implement input validation to enforce a valid discount rate range. This can be achieved by either raising a `ValueError` when the discount rate falls outside the acceptable bounds of 0.0 to 1.0, or by clamping the rate into that valid range. Additionally, prevent negative totals by ensuring the discounted subtotal never drops below 0.0 using a maximum-value constraint, similar to the pattern used in the absolute discount helper. Include documentation in the function's docstring that clarifies the allowed discount rate range and specifies whether out-of-range values trigger an exception or are automatically adjusted.

```
@@ -28,3 +28,14 @@ def calculate_total_with_discount(subtotal: float, sales_tax_rate: float, discou
 
     discounted_subtotal = max(subtotal - discount_amount, 0.0)
     return calculate_total(discounted_subtotal, sales_tax_rate=sales_tax_rate)
+
+
+def calculate_total_with_percentage_discount(
+    subtotal: float,
+    sales_tax_rate: float,
+    discount_rate: float,
+) -> float:
+    """Apply a percentage discount before tax."""
+
+    discounted_subtotal = subtotal * (1 - discount_rate)
+    return calculate_total(discounted_subtotal, sales_tax_rate=sales_tax_rate)
```

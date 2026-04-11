---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/7
pr_title: "feat: add capped percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/7#discussion_r3067724989
author: "Galzi1"
date: 2026-04-11T07:08:17+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 3067724989
---

# Negative discount caps and rates above 1.0 can silently invert discounts into surcharges or make subtotals negative while appearing mathematically correct.

## Symptom

Discount calculations may produce unexpected results when invalid parameters are used. A negative cap value or a discount rate exceeding 1.0 can cause the discount to function as a surcharge or reduce the subtotal to negative values, while the calculation still appears mathematically sound.

## Root Cause

The capped percentage discount helper lacks validation for its input parameters. Specifically, the `discount_rate` and `max_discount_amount` values are not checked for logical constraints before being applied to the calculation.

## Fix or Workaround

Validate both the `discount_rate` and `max_discount_amount` parameters before performing discount calculations. Ensure the discount rate does not exceed 1.0 and that the maximum discount amount is not negative, preventing silent conversion of the discount into a surcharge or subtotal inversion.

```
@@ -39,3 +39,16 @@ def calculate_total_with_percentage_discount(
 
     discounted_subtotal = subtotal * (1 - discount_rate)
     return calculate_total(discounted_subtotal, sales_tax_rate=sales_tax_rate)
+
+
+def calculate_total_with_capped_percentage_discount(
+    subtotal: float,
+    sales_tax_rate: float,
+    discount_rate: float,
+    max_discount_amount: float,
+) -> float:
+    """Apply a percentage discount before tax, capped by an absolute amount."""
+
+    discount_amount = min(subtotal * discount_rate, max_discount_amount)
```

---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/7
pr_title: "feat: add capped percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/7#discussion_r3067725989
author: "qodo-code-review[bot]"
date: 2026-04-11T07:09:35+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 3067725989
---

# Discount calculation can exceed subtotal and produce negative totals, unlike the clamped behavior in the similar function.

## Symptom

The `calculate_total_with_capped_percentage_discount()` function can produce negative discounted subtotals and negative total amounts. This occurs when the calculated discount amount exceeds the order subtotal, resulting in incorrect order totals.

## Root Cause

The function does not constrain the discount amount to not exceed the subtotal. Unlike the existing `calculate_total_with_discount()` function, which explicitly prevents discounted subtotals from going below zero, this new function lacks bounds checking on the discount calculation.

## Fix or Workaround

Apply bounds to both the discount amount and the resulting subtotal:

- Cap the discount amount to the minimum of: the percentage-based discount, the maximum discount allowed, and the subtotal itself
- Clamp the discounted subtotal to ensure it does not fall below zero
- Pass the bounded discounted subtotal to the existing `calculate_total()` function

This approach aligns the behavior with the existing discount function and prevents negative order totals.

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
+    discounted_subtotal = subtotal - discount_amount
+    return calculate_total(discounted_subtotal, sales_tax_rate=sales_tax_rate)
```

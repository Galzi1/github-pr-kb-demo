---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/7
pr_title: "feat: add capped percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/7#discussion_r3067725988
author: "qodo-code-review[bot]"
date: 2026-04-11T07:09:35+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 3067725988
---

# Negative max_discount_amount silently converts a discount into a surcharge by making discount_amount negative, exploiting an unvalidated input parameter.

## Symptom

The `calculate_total_with_capped_percentage_discount()` function can silently overcharge customers when a negative value is passed as the `max_discount_amount` parameter. Instead of applying a discount, the function converts it into a surcharge that increases the subtotal.

## Root Cause

The function does not validate the `max_discount_amount` parameter to ensure it is non-negative. When a negative value is provided, the calculation `min(subtotal * discount_rate, max_discount_amount)` selects the negative cap as the discount amount. This negative discount is then subtracted from the subtotal, resulting in an addition rather than a reduction. The codebase already enforces non-negative constraints on absolute discount amounts in other discount functions, but this validation was omitted from the capped percentage discount helper.

## Fix or Workaround

Add input validation to reject negative `max_discount_amount` values by raising a `ValueError` with an appropriate error message. Additionally, consider clamping the calculated `discount_amount` to ensure it never becomes negative, providing a defensive safeguard against similar issues.

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
```

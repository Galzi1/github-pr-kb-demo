---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/10
pr_title: "feat: add minimum charge helper for final demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/10#discussion_r3067728940
author: "Galzi1"
date: 2026-04-11T07:13:23+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 3067728940
---

# Minimum charge validation is missing, which can cause negative amounts or unintended charge increases when values are invalid.

## Symptom

The minimum charge helper can produce unexpected financial calculations. Specifically, it may generate negative pre-tax amounts or inadvertently increase charges beyond the intended minimum floor value.

## Root Cause

The minimum charge helper lacks validation for the minimum_charge parameter. When minimum_charge is set to a negative value or exceeds the subtotal amount, the helper's logic breaks down and produces incorrect monetary results.

## Fix or Workaround

Validate the minimum_charge parameter to ensure it falls within acceptable bounds—specifically, it should not be negative and should not exceed the subtotal. This validation prevents the helper from producing negative pre-tax amounts or incorrectly inflating charges.

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
```

---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1
pr_title: "feat: add discount pricing helper for review demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1#discussion_r3063857933
author: "qodo-code-review[bot]"
date: 2026-04-10T11:15:12+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 3063857933
---

# Discount amounts are not validated, allowing negative totals and tax calculations to propagate invalid charges downstream.

## Symptom

The `calculate_total_with_discount` function can produce negative total amounts and negative tax values. This occurs when the discount amount exceeds the subtotal, resulting in invalid charge amounts that may propagate through callers who expect non-negative totals.

## Root Cause

The function performs discount subtraction without validation constraints. The implementation subtracts `discount_amount` directly from `subtotal` without checking whether the discount exceeds the original subtotal value or whether the discount itself is negative. This allows the discounted subtotal to become negative, which then flows through to the total and tax calculations.

## Fix or Workaround

Three remediation approaches are available:

1. **Clamp to minimum**: Constrain the discounted subtotal to never go below zero using a maximum operation, ensuring totals remain non-negative regardless of discount magnitude.

2. **Validate inputs**: Implement input validation that raises an error if the discount amount is negative or exceeds the subtotal, rejecting invalid discount values at the function boundary.

3. **Support intentional credits**: If negative totals are intended for refund or credit scenarios, document this behavior explicitly in the function documentation and consider renaming parameters to clarify the semantic intent (such as `adjustment_amount` instead of `discount_amount`).

The affected code is located in demo_app.py at lines 12-14.

```
@@ -5,5 +5,10 @@ def greet(name: str) -> str:
     return f"Hello, {name}!"
 
 
-def calculate_total(subtotal: float, tax_rate: float) -> float:
-    return round(subtotal * (1 + tax_rate), 2)
+def calculate_total(subtotal: float, sales_tax_rate: float) -> float:
+    return round(subtotal * (1 + sales_tax_rate), 2)
+
+
+def calculate_total_with_discount(subtotal: float, sales_tax_rate: float, discount_amount: float) -> float:
+    discounted_subtotal = subtotal - discount_amount
+    return calculate_total(discounted_subtotal, sales_tax_rate)
```

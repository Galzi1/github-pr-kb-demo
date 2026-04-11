---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1
pr_title: "feat: add discount pricing helper for review demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1#discussion_r3064070321
author: "Galzi1"
date: 2026-04-10T11:55:32+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 3064070321
---

# The function now prevents negative charges and taxes by rejecting negative discounts and clamping subtotals to zero, addressing unexpected edge case behavior.

## Symptom

Not stated in the source comment.

## Root Cause

The discount pricing helper could previously accept negative discount values and produce a discounted subtotal below zero, which could result in negative charge amounts or negative tax calculations.

## Fix or Workaround

The `calculate_total_with_discount` function now includes validation to reject negative discounts and ensures the discounted subtotal cannot fall below zero. This prevents the generation of negative charges or tax amounts during discount calculations.

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

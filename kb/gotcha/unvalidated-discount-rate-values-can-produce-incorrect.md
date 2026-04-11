---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3
pr_title: "feat: add percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3#discussion_r3066907088
author: "Galzi1"
date: 2026-04-10T21:53:41+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 3066907088
---

# Unvalidated discount_rate values can produce incorrect pricing (surcharges or negative totals) while maintaining mathematical validity, making bugs hard to detect.

## Symptom

A percentage discount helper may produce unexpected pricing results, such as converting a discount into a surcharge or generating negative totals. These calculation errors can go undetected because the underlying mathematical formula appears valid.

## Root Cause

The discount rate parameter lacks validation or clamping logic to ensure values remain within the expected range. Out-of-range discount values cause the helper to operate incorrectly, producing incorrect pricing outcomes.

## Fix or Workaround

Validate or clamp the discount_rate parameter to ensure it remains within acceptable bounds before applying the discount calculation.

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
```

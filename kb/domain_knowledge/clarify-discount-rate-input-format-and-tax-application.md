---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3
pr_title: "feat: add percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3#discussion_r3066907152
author: "Galzi1"
date: 2026-04-10T21:53:43+00:00
category: domain_knowledge
confidence: 0.92
needs_review: false
comment_id: 3066907152
---

# Clarify discount_rate input format and tax application semantics in documentation since they directly affect invoice calculations.

## Context

A percentage discount helper function has been added as part of demo review functionality. This helper complements an existing absolute-discount helper with similar capabilities.

## Key Insight

The percentage discount helper requires explicit documentation of two critical business rules that are essential for correct invoice calculation:

1. The expected format of the discount rate parameter—specifically whether values should be provided in the range of 0 to 1 (decimal format) or another convention
2. The timing of tax application relative to the discount—whether the percentage discount is applied before or after tax calculations, consistent with how the absolute-discount helper operates

These specifications must be clearly stated in the function's docstring rather than left implicit in the implementation logic.

## Implications

The discount semantics directly impact invoice behavior and calculation results. Without explicit documentation of the discount rate format and tax application order, implementation details could be misinterpreted or applied inconsistently, leading to incorrect financial calculations in generated invoices.

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
```

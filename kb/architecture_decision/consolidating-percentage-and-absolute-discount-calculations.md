---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3
pr_title: "feat: add percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3#discussion_r3066907115
author: "Galzi1"
date: 2026-04-10T21:53:42+00:00
category: architecture_decision
confidence: 0.92
needs_review: false
comment_id: 3066907115
---

# Consolidating percentage and absolute discount calculations through a single normalization path reduces maintenance burden and prevents pricing logic divergence.

## Context

A percentage discount helper was needed for demo review purposes. The implementation required a decision about how to handle the calculation flow for percentage-based discounts in relation to existing discount processing.

## Decision

Percentage discounts are routed through the same normalization pathway as the existing absolute-discount helper rather than creating a separate calculation flow. This approach consolidates discount processing into a single shared path for handling validation, tax calculations, and rounding operations.

## Consequences

Maintaining a unified processing path for all discount types reduces the risk of pricing logic diverging between different discount calculation methods during future modifications. Centralized processing makes it easier to apply consistent rules and changes across all discount scenarios.

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

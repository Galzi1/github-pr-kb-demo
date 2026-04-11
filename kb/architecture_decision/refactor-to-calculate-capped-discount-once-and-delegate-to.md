---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/7
pr_title: "feat: add capped percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/7#discussion_r3067725001
author: "Galzi1"
date: 2026-04-11T07:08:18+00:00
category: architecture_decision
confidence: 0.92
needs_review: false
comment_id: 3067725001
---

# Refactor to calculate capped discount once and delegate to shared helper to avoid repeating pricing math and consolidate tax flow responsibility.

## Context

A new capped percentage discount helper is being added to support demo review functionality. The implementation requires handling both percentage-based discounts and ensuring they are properly constrained within acceptable bounds.

## Decision

The capped percentage discount calculation is delegated to the existing absolute-discount helper rather than implementing independent pricing mathematics. The percentage discount amount is calculated first, then passed to the calculate_total_with_discount function, allowing the absolute-discount path to maintain responsibility for clamping discount values and managing tax calculation flows.

## Consequences

This architectural approach consolidates pricing mathematics and discount clamping logic into a single code path, reducing duplication of discount calculation and tax handling logic across multiple helpers. The absolute-discount helper becomes the authoritative implementation for these concerns rather than having the logic replicated in percentage-based discount variants.

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

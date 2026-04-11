---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/7
pr_title: "feat: add capped percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/7#discussion_r3067725011
author: "Galzi1"
date: 2026-04-11T07:08:19+00:00
category: domain_knowledge
confidence: 0.92
needs_review: false
comment_id: 3067725011
---

# Discount calculation rules (pre/post-tax and scope) are business logic that must be explicitly documented to prevent invoice behavior misunderstandings.

## Context

A capped percentage discount helper feature has been added for demo review purposes. This helper function applies a percentage-based discount with a maximum limit.

## Key Insight

The behavior of the maximum discount amount parameter requires explicit documentation to prevent misunderstandings. Specifically, two aspects need clarification:

1. Whether the maximum discount amount represents a currency value calculated before or after tax application
2. Whether the cap operates at the order level (applying once across the entire order) or at the line item level (applying individually to each line item)

Currently, this information may only be inferrable from the implementation details rather than being clearly stated in the documentation.

## Implications

Not stated in the source comment.

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
```

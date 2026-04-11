---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1
pr_title: "feat: add discount pricing helper for review demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1#discussion_r3064005728
author: "Galzi1"
date: 2026-04-10T11:48:16+00:00
category: architecture_decision
confidence: 0.92
needs_review: false
comment_id: 3064005728
---

# Question about whether the discount API should support both absolute amounts and percentages, and the naming implications of choosing one representation.

## Context

A discount pricing helper was introduced to support the review demo feature. The implementation required deciding how to model discount values in the API, specifically whether to support only absolute currency amounts or to extend the model to include percentage-based discounts as well.

## Decision

Not stated in the source comment.

## Consequences

Not stated in the source comment.

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
```

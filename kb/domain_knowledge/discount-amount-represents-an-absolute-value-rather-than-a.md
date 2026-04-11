---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1
pr_title: "feat: add discount pricing helper for review demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1#discussion_r3064070542
author: "Galzi1"
date: 2026-04-10T11:55:34+00:00
category: domain_knowledge
confidence: 0.92
needs_review: false
comment_id: 3064070542
---

# discount_amount represents an absolute value rather than a percentage, with tax calculated post-discount; percentage discounts would be handled separately.

## Context

A discount pricing helper has been added to support review demo functionality. This helper is designed to handle discount calculations in a specific way.

## Key Insight

The discount pricing helper operates with two critical characteristics:

1. The discount amount parameter represents an absolute value in currency units, not a percentage of the original price
2. Tax calculation occurs after the discount is applied, meaning the tax is computed on the discounted price rather than the original price

## Implications

If percentage-based discounts are needed in the future, a separate helper function should be created rather than extending the existing helper to support both absolute and percentage discount types.

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

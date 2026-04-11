---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1
pr_title: "feat: add discount pricing helper for review demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1#discussion_r3063857930
author: "qodo-code-review[bot]"
date: 2026-04-10T11:15:11+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 3063857930
---

# Renaming a function parameter breaks backward compatibility for callers using keyword arguments, with no migration path provided.

## Symptom

Code that calls `calculate_total` using `tax_rate` as a keyword argument will fail with a `TypeError`. This occurs because the function parameter was renamed to `sales_tax_rate`, breaking any existing callers that reference the old parameter name.

## Root Cause

The `calculate_total` function's keyword parameter was renamed from `tax_rate` to `sales_tax_rate`. Since this function is exposed as a top-level helper in the module, external code that passes arguments by the old keyword name will no longer match any parameter and will raise an error.

## Fix or Workaround

Implement a compatibility shim that accepts both parameter names. Keep `sales_tax_rate` as the primary argument name while also supporting `tax_rate` as an optional keyword-only alias that maps to the new parameter. The implementation should reject cases where both names are provided simultaneously. Optionally, emit a `DeprecationWarning` when the old `tax_rate` parameter is used to guide callers toward the new naming convention.

```
@@ -5,5 +5,10 @@ def greet(name: str) -> str:
     return f"Hello, {name}!"
 
 
-def calculate_total(subtotal: float, tax_rate: float) -> float:
-    return round(subtotal * (1 + tax_rate), 2)
+def calculate_total(subtotal: float, sales_tax_rate: float) -> float:
+    return round(subtotal * (1 + sales_tax_rate), 2)
```

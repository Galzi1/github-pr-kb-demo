---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1
pr_title: "feat: add discount pricing helper for review demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1#discussion_r3064070142
author: "Galzi1"
date: 2026-04-10T11:55:31+00:00
category: architecture_decision
confidence: 0.82
needs_review: false
comment_id: 3064070142
---

# Chose to maintain backward compatibility through an alias while explicitly rejecting dual parameter usage to enforce a clear migration path.

## Context

Not stated in the source comment.

## Decision

The pricing helper was modified to establish a clear primary parameter name while maintaining backward compatibility. The parameter `sales_tax_rate` was designated as the primary name, with `tax_rate` added as a compatibility alias for existing callers using the older name. The implementation explicitly prevents simultaneous use of both parameter names to ensure the transition between naming conventions remains intentional and visible.

## Consequences

Callers using the older `tax_rate` parameter name will continue to function without modification. However, any code attempting to pass both `sales_tax_rate` and `tax_rate` simultaneously will be rejected by the helper, enforcing an explicit migration path for affected code.

```
@@ -5,5 +5,10 @@ def greet(name: str) -> str:
     return f"Hello, {name}!"
 
 
-def calculate_total(subtotal: float, tax_rate: float) -> float:
-    return round(subtotal * (1 + tax_rate), 2)
+def calculate_total(subtotal: float, sales_tax_rate: float) -> float:
+    return round(subtotal * (1 + sales_tax_rate), 2)
```

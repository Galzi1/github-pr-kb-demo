---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1
pr_title: "feat: add discount pricing helper for review demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1#issuecomment-4223263760
author: "qodo-code-review[bot]"
date: 2026-04-10T11:12:48+00:00
category: code_pattern
confidence: 0.75
needs_review: false
comment_id: 4223263760
---

# Adding a helper function for discount pricing calculations that applies discounts before tax computation.

## Pattern

This pattern implements pricing calculation helpers that support both standard and discounted pricing scenarios. The implementation involves a parameter rename for clarity and the addition of a new function to handle discount applications.

The existing calculation function uses a sales tax rate parameter (renamed from the previous `tax_rate` designation) to compute totals with tax applied. A new complementary function extends this capability by accepting a discount amount that is subtracted from the subtotal before tax calculation is performed.

The two functions work together, with the discount-aware function leveraging the tax calculation logic of the original function to produce the final discounted total with tax included.

## When to Use

Not stated in the source comment.

## Example

Not stated in the source comment.

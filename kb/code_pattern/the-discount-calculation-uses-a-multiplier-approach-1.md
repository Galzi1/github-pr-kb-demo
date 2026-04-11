---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3
pr_title: "feat: add percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3#issuecomment-4226957527
author: "qodo-code-review[bot]"
date: 2026-04-10T21:42:21+00:00
category: code_pattern
confidence: 0.78
needs_review: false
comment_id: 4226957527
---

# The discount calculation uses a multiplier approach (1 - discount_rate) rather than direct subtraction, which is a common pattern for composable percentage calculations.

## Pattern

A percentage discount helper function applies discounts to a subtotal before tax calculation. The function accepts three parameters: the subtotal amount, a sales tax rate, and a discount rate. It calculates the discounted subtotal using a multiplier approach by multiplying the subtotal by (1 - discount_rate). The resulting discounted subtotal is then passed to an existing total calculation function that applies the sales tax rate to produce the final total.

## When to Use

This pattern is useful in pricing calculation workflows where percentage-based discounts need to be applied before tax computation. It provides a dedicated helper function that separates discount logic from tax calculation, making the pricing computation more modular and easier to review.

## Example

Not stated in the source comment.

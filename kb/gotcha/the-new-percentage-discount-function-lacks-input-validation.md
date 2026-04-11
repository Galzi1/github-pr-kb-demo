---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3
pr_title: "feat: add percentage discount helper for demo review"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/3#issuecomment-4226957619
author: "qodo-code-review[bot]"
date: 2026-04-10T21:42:22+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 4226957619
---

# The new percentage discount function lacks input validation, allowing negative discount rates to increase totals and rates above 1.0 to produce negative totals, unlike the existing absolute discount h

## Symptom

The `calculate_total_with_percentage_discount` function can produce unexpected results when provided with invalid discount rates. If the discount rate exceeds 1.0, the function returns a negative total. If the discount rate is negative, the function increases the subtotal instead of applying a discount, contrary to its intended behavior.

## Root Cause

The function performs the calculation `subtotal * (1 - discount_rate)` without validating the input parameter `discount_rate`. Unlike the existing `calculate_total_with_discount` helper function, which validates the discount parameter and clamps the result to prevent negative subtotals, the new percentage discount helper lacks these protective measures. The function passes the computed discounted subtotal directly to `calculate_total`, which does not enforce a minimum value of zero.

## Fix or Workaround

Implement input validation on the `discount_rate` parameter to enforce a valid range. Either raise a `ValueError` when the discount rate falls outside the range of 0.0 to 1.0 (inclusive), or clamp the value into that valid range. Additionally, apply a safety check similar to the existing absolute discount helper by ensuring the discounted subtotal does not fall below zero using a maximum operation. Update the function's docstring to document the expected input range for `discount_rate` and describe the behavior when values fall outside this range.

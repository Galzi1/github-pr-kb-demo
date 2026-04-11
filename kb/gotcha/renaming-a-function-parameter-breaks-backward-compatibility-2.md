---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1
pr_title: "feat: add discount pricing helper for review demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1#issuecomment-4223264048
author: "qodo-code-review[bot]"
date: 2026-04-10T11:12:49+00:00
category: gotcha
confidence: 0.92
needs_review: false
comment_id: 4223264048
---

# Renaming a function parameter breaks backward compatibility for callers using keyword arguments without providing a deprecation path.

## Symptom

The `calculate_total_with_discount` function allows discount amounts to exceed the subtotal, resulting in negative discounted subtotals. This causes the function to return negative totals (including negative tax amounts), which can propagate invalid charge amounts downstream if callers assume the returned values are non-negative.

## Root Cause

The function performs subtraction of the discount amount from the subtotal without any validation or bounds checking. When the discount amount is greater than the subtotal, the intermediate `discounted_subtotal` value becomes negative, and this negative value is passed directly to `calculate_total`, which applies the tax calculation and rounding to the invalid intermediate result.

## Fix or Workaround

Three approaches are suggested:

**Option 1 (Clamp):** Cap the discounted subtotal at zero using `max(subtotal - discount_amount, 0.0)` to ensure totals never go below zero.

**Option 2 (Validate and raise):** Add validation to reject cases where `discount_amount` is negative or exceeds `subtotal` by raising a `ValueError`.

**Option 3 (Support credits/refunds):** If negative totals are intentionally supported as refunds or credits, document this behavior in a docstring and consider renaming parameters (such as `adjustment_amount`) to clarify intent.

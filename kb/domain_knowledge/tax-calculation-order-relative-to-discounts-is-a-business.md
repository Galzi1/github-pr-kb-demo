---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1
pr_title: "feat: add discount pricing helper for review demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1#issuecomment-4223530384
author: "Galzi1"
date: 2026-04-10T11:48:28+00:00
category: domain_knowledge
confidence: 0.92
needs_review: false
comment_id: 4223530384
---

# Tax calculation order relative to discounts is a business rule that needs explicit documentation.

## Context

A discount pricing helper has been added to support review demonstrations. This helper processes pricing calculations that involve both discounts and taxes.

## Key Insight

The current implementation applies tax calculations to the subtotal after discounts have been applied. This approach treats the discount as reducing the taxable base amount.

## Implications

This tax-after-discount sequencing should be documented explicitly as a business rule to ensure clarity around how pricing is calculated when both discounts and taxes are involved in transactions.

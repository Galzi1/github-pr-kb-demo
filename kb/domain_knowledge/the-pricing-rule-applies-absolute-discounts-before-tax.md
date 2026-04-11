---
pr_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1
pr_title: "feat: add discount pricing helper for review demo"
comment_url: https://github.com/Galzi1/github-pr-kb-demo/pull/1#issuecomment-4223569372
author: "Galzi1"
date: 2026-04-10T11:55:35+00:00
category: domain_knowledge
confidence: 0.92
needs_review: false
comment_id: 4223569372
---

# The pricing rule applies absolute discounts before tax calculation, with the business logic now documented in code and demonstrated in test cases.

## Context

A discount pricing helper was added to support a review demonstration. This implementation follows up on a previous discussion regarding pricing rules and makes the business logic explicit within the code documentation.

## Key Insight

The discount pricing helper applies discounts in a specific sequence: an absolute discount is applied to the original subtotal first, and then tax is calculated on the discounted amount rather than the original price. This ordering ensures the demonstration accurately reflects the intended pricing behavior.

## Implications

Not stated in the source comment.

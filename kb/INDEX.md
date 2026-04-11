# Knowledge Base Index

## Architecture Decision (3)

- [Chose to maintain backward compatibility through an alias while explicitly rejecting dual parameter usage to enforce a clear migration path.](architecture_decision/chose-to-maintain-backward-compatibility-through-an-alias.md)
- [Consolidating percentage and absolute discount calculations through a single normalization path reduces maintenance burden and prevents pricing logic divergence.](architecture_decision/consolidating-percentage-and-absolute-discount-calculations.md)
- [Question about whether the discount API should support both absolute amounts and percentages, and the naming implications of choosing one representation.](architecture_decision/question-about-whether-the-discount-api-should-support-both.md)

## Code Pattern (2)

- [Adding a helper function for discount pricing calculations that applies discounts before tax computation.](code_pattern/adding-a-helper-function-for-discount-pricing-calculations.md)
- [The discount calculation uses a multiplier approach (1 - discount_rate) rather than direct subtraction, which is a common pattern for composable percentage calculations.](code_pattern/the-discount-calculation-uses-a-multiplier-approach-1.md)

## Domain Knowledge (4)

- [Clarify discount_rate input format and tax application semantics in documentation since they directly affect invoice calculations.](domain_knowledge/clarify-discount-rate-input-format-and-tax-application.md)
- [discount_amount represents an absolute value rather than a percentage, with tax calculated post-discount; percentage discounts would be handled separately.](domain_knowledge/discount-amount-represents-an-absolute-value-rather-than-a.md)
- [Tax calculation order relative to discounts is a business rule that needs explicit documentation.](domain_knowledge/tax-calculation-order-relative-to-discounts-is-a-business.md)
- [The pricing rule applies absolute discounts before tax calculation, with the business logic now documented in code and demonstrated in test cases.](domain_knowledge/the-pricing-rule-applies-absolute-discounts-before-tax.md)

## Gotcha (7)

- [Discount amounts are not validated, allowing negative totals and tax calculations to propagate invalid charges downstream.](gotcha/discount-amounts-are-not-validated-allowing-negative-totals.md)
- [Renaming a function parameter breaks backward compatibility for callers using keyword arguments, with no migration path provided.](gotcha/renaming-a-function-parameter-breaks-backward-compatibility.md)
- [Renaming a function parameter breaks backward compatibility for callers using keyword arguments without providing a deprecation path.](gotcha/renaming-a-function-parameter-breaks-backward-compatibility-2.md)
- [The function now prevents negative charges and taxes by rejecting negative discounts and clamping subtotals to zero, addressing unexpected edge case behavior.](gotcha/the-function-now-prevents-negative-charges-and-taxes-by.md)
- [The new percentage discount function lacks input validation, allowing negative discount rates to increase totals and rates above 1.0 to produce negative totals, unlike the existing absolute discount h](gotcha/the-new-percentage-discount-function-lacks-input-validation.md)
- [Unbounded discount_rate parameter can produce negative totals or unintended surcharges due to missing input validation, unlike the similar absolute discount function that includes guards.](gotcha/unbounded-discount-rate-parameter-can-produce-negative.md)
- [Unvalidated discount_rate values can produce incorrect pricing (surcharges or negative totals) while maintaining mathematical validity, making bugs hard to detect.](gotcha/unvalidated-discount-rate-values-can-produce-incorrect.md)

## Other (2)

- [This is a placeholder message from an automated code review tool indicating analysis is in progress.](other/this-is-a-placeholder-message-from-an-automated-code-review.md)
- [This is an automated review summary documenting the creation of a knowledge base with 16 categorized insights from pricing helper PR reviews, organized into architecture decisions, code patterns, doma](other/this-is-an-automated-review-summary-documenting-the.md)

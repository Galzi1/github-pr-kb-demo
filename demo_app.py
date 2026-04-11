"""Tiny file for github-pr-kb demo pull requests."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def calculate_total(subtotal: float, sales_tax_rate: float | None = None, *, tax_rate: float | None = None) -> float:
    """Return the taxed total.

    `tax_rate` remains accepted as a compatibility alias for older keyword callers.
    """

    if sales_tax_rate is None and tax_rate is None:
        raise TypeError("calculate_total() requires sales_tax_rate or tax_rate")
    if sales_tax_rate is not None and tax_rate is not None:
        raise TypeError("Pass either sales_tax_rate or tax_rate, not both")

    effective_tax_rate = tax_rate if sales_tax_rate is None else sales_tax_rate
    return round(subtotal * (1 + effective_tax_rate), 2)


def calculate_total_with_discount(subtotal: float, sales_tax_rate: float, discount_amount: float) -> float:
    """Apply an absolute discount amount before tax and never return a negative total."""

    if discount_amount < 0:
        raise ValueError("discount_amount must be non-negative")

    discounted_subtotal = max(subtotal - discount_amount, 0.0)
    return calculate_total(discounted_subtotal, sales_tax_rate=sales_tax_rate)


def calculate_total_with_percentage_discount(
    subtotal: float,
    sales_tax_rate: float,
    discount_rate: float,
) -> float:
    """Apply a percentage discount before tax."""

    discounted_subtotal = subtotal * (1 - discount_rate)
    return calculate_total(discounted_subtotal, sales_tax_rate=sales_tax_rate)


def calculate_total_with_capped_percentage_discount(
    subtotal: float,
    sales_tax_rate: float,
    discount_rate: float,
    max_discount_amount: float,
) -> float:
    """Apply a percentage discount before tax, capped by an absolute amount."""

    discount_amount = min(subtotal * discount_rate, max_discount_amount)
    discounted_subtotal = subtotal - discount_amount
    return calculate_total(discounted_subtotal, sales_tax_rate=sales_tax_rate)


def calculate_total_with_minimum_charge(
    subtotal: float,
    sales_tax_rate: float,
    discount_amount: float,
    minimum_charge: float = 0.0,
) -> float:
    """Apply a discount before tax, but never reduce the subtotal below a floor."""

    adjusted_subtotal = max(subtotal - discount_amount, minimum_charge)
    return calculate_total(adjusted_subtotal, sales_tax_rate=sales_tax_rate)

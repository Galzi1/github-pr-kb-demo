"""Tiny file for github-pr-kb demo pull requests."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def calculate_total(subtotal: float, sales_tax_rate: float) -> float:
    return round(subtotal * (1 + sales_tax_rate), 2)


def calculate_total_with_discount(subtotal: float, sales_tax_rate: float, discount_amount: float) -> float:
    discounted_subtotal = subtotal - discount_amount
    return calculate_total(discounted_subtotal, sales_tax_rate)

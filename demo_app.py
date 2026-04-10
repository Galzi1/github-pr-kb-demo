"""Tiny file for github-pr-kb demo pull requests."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def calculate_total(subtotal: float, tax_rate: float) -> float:
    return round(subtotal * (1 + tax_rate), 2)

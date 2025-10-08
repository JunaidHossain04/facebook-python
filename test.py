"""Utility functions and CLI entry-point for simple arithmetic tasks."""

from __future__ import annotations

import argparse
from numbers import Real
from typing import Tuple


def _validate_number(value: Real) -> None:
    """Ensure the provided value behaves like a real number but is not a bool."""
    if not isinstance(value, Real) or isinstance(value, bool):
        raise TypeError("Both arguments must be real numbers (int or float, not bool)")


def calculate_sum(a: Real, b: Real) -> float:
    """Calculate the sum of two numbers with input validation.

    Args:
        a (Real): First number.
        b (Real): Second number.

    Returns:
        float: The sum of *a* and *b*.

    Raises:
        TypeError: If either *a* or *b* is not a valid real number.
    """
    _validate_number(a)
    _validate_number(b)

    return float(a + b)


def parse_args() -> Tuple[float, float]:
    """Parse command-line arguments for the CLI."""
    parser = argparse.ArgumentParser(description="Calculate the sum of two numbers.")
    parser.add_argument("a", type=float, help="First number.")
    parser.add_argument("b", type=float, help="Second number.")
    args = parser.parse_args()
    return args.a, args.b


def main() -> None:
    """Entry-point for the CLI: parse inputs, compute the sum, and display it."""
    try:
        a, b = parse_args()
        total = calculate_sum(a, b)
        print(f"Sum: {total}")
    except TypeError as error:
        print(f"Error: {error}")
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()

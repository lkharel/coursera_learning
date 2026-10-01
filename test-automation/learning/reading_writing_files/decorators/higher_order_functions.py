"""Examples of higher-order functions."""

from collections.abc import Callable


def one() -> int:
    """Return one."""
    return 1


def add(first: int, second: int) -> int:
    """Return the sum of two integers."""
    return first + second


def subtract(first: int, second: int) -> int:
    """Return the difference between two integers."""
    return first - second


def calculate(
    func: Callable[[int, int], int],
    first: int,
    second: int,
) -> int:
    """Apply a two-argument function to two integers."""
    return func(first, second)


if __name__ == "__main__":
    print(type(one))
    print(calculate(add, 2, 5))
    print(calculate(subtract, 2, 5))

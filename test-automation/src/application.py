"""Small application used to demonstrate pytest test automation."""


def add(first_number: float, second_number: float) -> float:
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number: float, second_number: float) -> float:
    """Return the difference between two numbers."""
    return first_number - second_number


def multiply(first_number: float, second_number: float) -> float:
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number: float, second_number: float) -> float:
    """Return the quotient and reject division by zero."""
    if second_number == 0:
        raise ValueError("Cannot divide by zero")
    return first_number / second_number


def is_even(number: int) -> bool:
    """Return True when an integer is even."""
    return number % 2 == 0

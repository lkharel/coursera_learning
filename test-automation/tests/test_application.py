"""Tests for the functions in src/application.py."""

import pytest

from src.application import add, divide, is_even, multiply, subtract


def test_add(sample_numbers: tuple[int, int]) -> None:
    first_number, second_number = sample_numbers
    assert add(first_number, second_number) == 15


def test_subtract(sample_numbers: tuple[int, int]) -> None:
    first_number, second_number = sample_numbers
    assert subtract(first_number, second_number) == 5


def test_multiply(sample_numbers: tuple[int, int]) -> None:
    first_number, second_number = sample_numbers
    assert multiply(first_number, second_number) == 50


def test_divide(sample_numbers: tuple[int, int]) -> None:
    first_number, second_number = sample_numbers
    assert divide(first_number, second_number) == 2


def test_divide_by_zero_raises_error() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


@pytest.mark.parametrize(
    ("first_number", "second_number", "expected"),
    [(1, 2, 3), (-1, 1, 0), (2.5, 1.5, 4.0)],
)
def test_add_with_multiple_values(
    first_number: float,
    second_number: float,
    expected: float,
) -> None:
    assert add(first_number, second_number) == expected


@pytest.mark.parametrize(
    ("number", "expected"),
    [(2, True), (3, False), (0, True), (-4, True)],
)
def test_is_even(number: int, expected: bool) -> None:
    assert is_even(number) is expected

"""Append sample text to a file beside this script."""

from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent / "my_first_file.txt"


def append_sample_line() -> None:
    """Append one line to the sample file."""
    with FILE_PATH.open("a", encoding="utf-8") as file:
        file.write("Second line is the best line!\n")


if __name__ == "__main__":
    append_sample_line()

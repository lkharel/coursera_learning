"""Write sample text to a file beside this script."""

from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent / "my_first_file.txt"


def write_sample_file() -> None:
    """Overwrite the sample file with example lines."""
    lines = [
        "Hello File\n",
        "Second line\n",
        "Hello File\n",
        "Hello File\n",
        "Hello File\n",
    ]
    FILE_PATH.write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    write_sample_file()

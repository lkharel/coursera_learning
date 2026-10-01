"""Shared pytest fixtures."""

import os
from pathlib import Path

import pytest

from log_processor.log_parser import LogParser


@pytest.fixture(scope="session")
def log_parser() -> LogParser:
    """Return a parser for the configured run directory."""
    default_directory = (
        Path(__file__).resolve().parents[1] / "log_processor" / "sample_logs"
    )
    run_directory = Path(os.getenv("RUN_DIRECTORY", str(default_directory)))
    return LogParser(run_directory)


@pytest.fixture
def sample_numbers() -> tuple[int, int]:
    """Return reusable numbers for arithmetic tests."""
    return 10, 5

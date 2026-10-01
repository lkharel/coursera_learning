"""Parse preprocessing logs and search sender/recipient pairs."""

from pathlib import Path


class LogParser:
    """Read log content after the header separator."""

    HEADER_END = "------------------------"
    LOG_PATTERN = "sample_pre_processing*.log"

    def __init__(self, run_directory: str | Path) -> None:
        self.run_directory = Path(run_directory)
        self.log_file = self._find_log_file()
        self.log_lines = self._read_log_lines()

    def _find_log_file(self) -> Path:
        """Return the first matching preprocessing log file."""
        try:
            return next(self.run_directory.glob(self.LOG_PATTERN))
        except StopIteration:
            raise FileNotFoundError(
                f"No {self.LOG_PATTERN} file found in " f"{self.run_directory}"
            ) from None

    def _read_log_lines(self) -> list[str]:
        """Return non-empty lines after the header separator."""
        log_lines = []
        start_reading = False

        with self.log_file.open(
            "r",
            encoding="utf-8",
            errors="ignore",
        ) as file:
            for line in file:
                line = line.strip()

                if not start_reading:
                    if line == self.HEADER_END:
                        start_reading = True
                    continue

                if line:
                    log_lines.append(line)

        if not start_reading:
            raise ValueError(
                f"Header separator '{self.HEADER_END}' was not found "
                f"in {self.log_file}"
            )

        return log_lines

    def contains_sender_recipient(
        self,
        sender: str,
        recipient: str,
    ) -> bool:
        """Return True when one log line contains both values."""
        for line in self.log_lines:
            if sender in line and recipient in line:
                return True

        return False

    def find_sender_recipient(
        self,
        sender: str,
        recipient: str,
    ) -> list[str]:
        """Return all log lines containing both values."""
        matches = []

        for line in self.log_lines:
            if sender in line and recipient in line:
                matches.append(line)

        return matches

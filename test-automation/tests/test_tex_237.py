"""Validate that at least one approved sender/recipient pair exists."""

import pytest

from log_processor.elements import RECIPIENT, SENDER


@pytest.mark.parametrize(
    "scenario, senders, recipients",
    [
        pytest.param(
            "Validate sender recipient pairs",
            SENDER,
            RECIPIENT,
            id="Validate_sender_recipient",
        ),
    ],
)
def test_expected_sender_recipient_exists(
    log_parser,
    scenario: str,
    senders: dict[str, str],
    recipients: dict[str, str],
) -> None:
    matched_pair = None

    for sender_name, sender_value in senders.items():
        for recipient_name, recipient_value in recipients.items():
            if log_parser.contains_sender_recipient(
                sender_value,
                recipient_value,
            ):
                matched_pair = (
                    sender_name,
                    recipient_name,
                    sender_value,
                    recipient_value,
                )
                break

        if matched_pair:
            break

    assert matched_pair, (
        f"{scenario}: no approved sender/recipient pair "
        "was found in the log file."
    )

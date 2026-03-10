import pytest

from pipeline.validate import validate_rows


def test_validate_rows_accepts_valid_data() -> None:
    rows = [
        {
            "customer_id": "1",
            "email": "user@example.com",
            "amount": "25.50",
            "order_date": "2026-03-01",
        }
    ]

    validate_rows(rows)


def test_validate_rows_rejects_invalid_email() -> None:
    rows = [
        {
            "customer_id": "1",
            "email": "invalid-email",
            "amount": "25.50",
            "order_date": "2026-03-01",
        }
    ]

    with pytest.raises(ValueError, match="invalid email address"):
        validate_rows(rows)

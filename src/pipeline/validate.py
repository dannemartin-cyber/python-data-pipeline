"""
File: validate.py

Purpose:
Validate incoming business data before transformation.

Responsibilities:
- confirm required columns are present
- check for empty required fields
- validate email formatting at a basic level
- ensure numeric fields can be processed
"""

from __future__ import annotations

REQUIRED_FIELDS = {"customer_id", "email", "amount", "order_date"}


def validate_rows(rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError("No rows found in input data")

    missing_fields = REQUIRED_FIELDS - set(rows[0].keys())
    if missing_fields:
        raise ValueError(
            f"Missing required columns: {sorted(missing_fields)}"
        )

    for row_number, row in enumerate(rows, start=1):
        if not row["customer_id"].strip():
            raise ValueError(f"Row {row_number}: customer_id is empty")

        if "@" not in row["email"]:
            raise ValueError(f"Row {row_number}: invalid email address")

        try:
            float(row["amount"])
        except ValueError as exc:
            raise ValueError(
                f"Row {row_number}: amount must be numeric"
            ) from exc

        if not row["order_date"].strip():
            raise ValueError(f"Row {row_number}: order_date is empty")

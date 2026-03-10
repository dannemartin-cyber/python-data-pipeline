from __future__ import annotations

from datetime import datetime


def transform_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    cleaned_rows: list[dict[str, str]] = []

    for row in rows:
        normalized_email = row["email"].strip().lower()
        normalized_amount = f"{float(row['amount']):.2f}"

        order_date = row["order_date"].strip()
        try:
            normalized_order_date = datetime.fromisoformat(order_date).date().isoformat()
        except ValueError:
            normalized_order_date = order_date

        cleaned_rows.append(
            {
                **row,
                "email": normalized_email,
                "amount": normalized_amount,
                "order_date": normalized_order_date,
            }
        )

    return cleaned_rows

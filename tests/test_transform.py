from pipeline.transform import transform_rows


def test_transform_normalizes_email_and_amount() -> None:
    rows = [
        {
            "customer_id": "1",
            "email": " TEST@EXAMPLE.COM ",
            "amount": "10",
            "order_date": "2026-03-01",
        }
    ]

    result = transform_rows(rows)

    assert result[0]["email"] == "test@example.com"
    assert result[0]["amount"] == "10.00"
    assert result[0]["order_date"] == "2026-03-01"

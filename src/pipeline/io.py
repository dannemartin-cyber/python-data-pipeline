"""
File: io.py

Purpose:
Handle CSV file input and output for the data pipeline.

Responsibilities:
- read raw CSV input data
- write cleaned output data
- ensure output directories exist when needed
"""

from __future__ import annotations

import csv
from pathlib import Path


def read_csv(path: str) -> list[dict[str, str]]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    with file_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(path: str, rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError("No rows to write")

    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = list(rows[0].keys())

    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

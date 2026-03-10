"""
File: cli.py

Purpose:
Provide a command-line interface for running the data pipeline.

Responsibilities:
- accept input and output file paths
- execute the pipeline workflow
- coordinate reading, validation, transformation, and output writing
"""

from __future__ import annotations

import argparse

from pipeline.io import read_csv, write_csv
from pipeline.validate import validate_rows
from pipeline.transform import transform_rows


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a simple business data pipeline on CSV input."
    )
    parser.add_argument(
        "--in",
        dest="input_path",
        required=True,
        help="Path to input CSV file",
    )
    parser.add_argument(
        "--out",
        dest="output_path",
        required=True,
        help="Path to cleaned output CSV file",
    )
    args = parser.parse_args()

    rows = read_csv(args.input_path)
    validate_rows(rows)
    cleaned_rows = transform_rows(rows)
    write_csv(args.output_path, cleaned_rows)

    print(f"Pipeline complete. Cleaned file written to: {args.output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from pipeline.logging_config import configure_logging

configure_logging()

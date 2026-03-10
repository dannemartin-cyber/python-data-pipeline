# Python Data Pipeline

Business-focused Python portfolio project demonstrating practical ETL-style processing, validation, transformation, and maintainable code structure.

---

## What this project covers

* CSV input and output
* validation-first processing
* transformation and normalization
* command-line execution
* testable and maintainable project structure
* business-oriented data workflow design

---

## Project structure

```text
python-data-pipeline/
  README.md
  pyproject.toml
  src/
    pipeline/
      __init__.py
      cli.py
      io.py
      validate.py
      transform.py
  data/
    raw/
      sample.csv
    out/
      .gitkeep
  tests/
    test_validate.py
    test_transform.py
```

---

## Goal

Show practical Python ability through structured, reusable, and testable code rather than one-off scripts.

---

## Business Scenario

This project simulates a lightweight business data pipeline that ingests raw CSV order data, validates required fields, standardizes values, and writes cleaned output for downstream reporting or analytics use.

Example business uses include:

* preparing sales data for reporting
* cleaning customer records
* validating data before import into a database
* standardizing business data for dashboards

---

## Key Python Techniques Demonstrated

* modular package structure
* file input and output handling
* argument parsing with `argparse`
* validation and exception handling
* transformation logic
* unit testing with `pytest`

---

## Example Workflow

1. Read raw business data from a CSV file
2. Validate required columns and field formats
3. Normalize values such as email addresses and numeric amounts
4. Write cleaned records to a new output file
5. Run tests to confirm expected behavior

---

## How to use this repo

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

For Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

### Run the pipeline

```bash
python -m pipeline.cli --in data/raw/sample.csv --out data/out/clean.csv
```

### Run tests

```bash
pytest
```

---

## Tech

Python 3

---

## Status

In progress — expanding with stronger validation rules, logging, and additional pipeline features.

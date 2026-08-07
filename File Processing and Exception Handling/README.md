# File Processing and Exception Handling

## Description
This project demonstrates how to read and process vehicle data from CSV and JSON files. It validates records, handles file-related exceptions, logs invalid entries, and exports valid records to a clean report.

## Features
- Read vehicle data from CSV
- Read vehicle data from JSON
- Validate required fields
- Handle file exceptions
- Log rejected records
- Export valid records to a clean CSV report
- File path management using pathlib

## Project Files

- main.py
- vehicle_events.csv
- vehicle_events.json
- clean_report.csv
- error.log

## Concepts Used

- `with open()`
- `csv`
- `json`
- `pathlib`
- `try`
- `except`
- `else`
- `finally`
- `logging`

## How to Run

```bash
python main.py
```

## Output

- Reads vehicle data from CSV and JSON files.
- Displays valid vehicle records.
- Creates `clean_report.csv`.
- Logs invalid records in `error.log`.

## Learning Outcome

- Learned file handling using CSV and JSON.
- Applied exception handling for reliable programs.
- Logged invalid records using the logging module.
- Exported validated data into a clean report.
- Used pathlib for file path management.
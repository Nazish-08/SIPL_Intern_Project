# Day 4 - Files, JSON, CSV and Exceptions

## Description
This project reads vehicle data from CSV and JSON files, validates the records, logs invalid entries, and exports valid records to a clean CSV report.

## Features
- Read data from CSV file
- Read data from JSON file
- Validate required fields
- Handle file exceptions
- Log rejected records
- Export valid records to clean_report.csv
- Use pathlib for file handling

## Files
- main.py
- vehicle_events.csv
- vehicle_events.json
- clean_report.csv
- error.log

## Concepts Used
- with open()
- csv
- json
- pathlib
- try
- except
- else
- finally
- logging

## How to Run

```bash
python main.py
```

## Output
- Displays valid vehicle records.
- Creates clean_report.csv.
- Logs invalid records in error.log.
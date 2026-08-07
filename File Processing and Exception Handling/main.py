import csv
import json
import logging
from pathlib import Path

# Logging Configuration
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File Paths
csv_file = Path("vehicle_events.csv")
json_file = Path("vehicle_events.json")
clean_file = Path("clean_report.csv")

valid_records = []

# Read CSV File
try:
    with open(csv_file, "r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if row["vehicle"] and row["gate"] and row["tat"]:
                valid_records.append(row)
            else:
                logging.error(f"Rejected Row: {row}")

except FileNotFoundError:
    print("CSV file not found.")

else:
    print("CSV file read successfully.")

finally:
    print("CSV processing completed.")

# Read JSON File
try:
    with open(json_file, "r") as file:
        json_data = json.load(file)

        print("\nReading JSON File")
        for record in json_data:
            print(record)

except FileNotFoundError:
    print("JSON file not found.")

else:
    print("JSON file read successfully.")

finally:
    print("JSON processing completed.")

# Display Valid Records
print("\nValid Records")
for record in valid_records:
    print(record)

# Export Valid Records to CSV
with open(clean_file, "w", newline="") as file:
    fieldnames = ["vehicle", "gate", "tat"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(valid_records)

print("\nClean report generated successfully.")
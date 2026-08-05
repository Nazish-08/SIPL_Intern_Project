vehicle_events = [
    {"vehicle": "MH12AB1234", "gate": "Gate-1", "tat": 18},
    {"vehicle": "DL05XY9876", "gate": "Gate-2", "tat": 25},
    {"vehicle": "", "gate": "Gate-1", "tat": 15},
    {"vehicle": "KA09PQ4567", "gate": "Gate-1", "tat": 30},
    {"vehicle": "MH14CD1111", "gate": "Gate-2", "tat": 20},
]

# Step 1: Print all records
print("All Records:")
print(vehicle_events)

# Step 2: Filter valid records
valid_records = []

for record in vehicle_events:
    if record["vehicle"] != "":
        valid_records.append(record)

# Step 3: Count vehicles by gate

gate_count = {}

for record in valid_records:
    gate = record["gate"]

    if gate in gate_count:
        gate_count[gate] += 1
    else:
        gate_count[gate] = 1

print("\nGate Wise Count:")
print(gate_count)

print("\nValid Records:")
print(valid_records)
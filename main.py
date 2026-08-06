from validation import validate_records
from calculation import count_by_gate, calculate_average_tat
from reporting import print_report


vehicle_events = [
    {"vehicle": "MH12AB1234", "gate": "Gate-1", "tat": 18},
    {"vehicle": "DL05XY9876", "gate": "Gate-2", "tat": 25},
    {"vehicle": "", "gate": "Gate-1", "tat": 15},
    {"vehicle": "KA09PQ4567", "gate": "Gate-1", "tat": 30},
    {"vehicle": "MH14CD1111", "gate": "Gate-2", "tat": 20},
]


def main():
    valid_records = validate_records(vehicle_events)
    gate_count = count_by_gate(valid_records)
    average_tat = calculate_average_tat(valid_records)

    print_report(
        len(vehicle_events),
        valid_records,
        gate_count,
        average_tat
    )


if __name__ == "__main__":
    main()
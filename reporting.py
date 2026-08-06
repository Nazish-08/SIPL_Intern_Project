def print_report(total_records, valid_records, gate_count, average_tat):
    """Print the vehicle summary report."""

    print("========== Vehicle Summary ==========")
    print()

    print("Total Records :", total_records)
    print("Valid Records :", len(valid_records))
    print("Invalid Records :", total_records - len(valid_records))

    print("\nGate Wise Count")
    for gate, count in gate_count.items():
        print(gate, ":", count)

    print("\nAverage TAT :", average_tat, "minutes")
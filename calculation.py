def count_by_gate(valid_records: list) -> dict:
    """Count vehicles by gate."""

    gate_count = {}

    for record in valid_records:
        gate = record["gate"]

        if gate in gate_count:
            gate_count[gate] += 1
        else:
            gate_count[gate] = 1

    return gate_count


def calculate_average_tat(valid_records: list) -> float:
    """Calculate average TAT."""

    total_tat = 0

    for record in valid_records:
        total_tat += record["tat"]

    return total_tat / len(valid_records)
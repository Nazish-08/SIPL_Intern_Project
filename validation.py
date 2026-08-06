def validate_records(vehicle_events):
    """Return only valid vehicle records."""

    valid_records = []

    for record in vehicle_events:
        if record["vehicle"] != "":
            valid_records.append(record)

    return valid_records
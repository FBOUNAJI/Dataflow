def remove_duplicates(data):

    seen = set()
    unique_data = []

    for record in data:
        record_tuple = tuple(record.items())

        if record_tuple not in seen:
            seen.add(record_tuple)
            unique_data.append(record)

    return unique_data
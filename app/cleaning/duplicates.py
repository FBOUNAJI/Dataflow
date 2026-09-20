def find_duplicates(data):

    seen = set()
    duplicates = []

    for index, record in enumerate(data, start=2):
        record_tuple = tuple(record.items())

        if record_tuple in seen:
            duplicates.append({
                "row": index,
                "record": record
            })
        else:
            
            seen.add(record_tuple)

    return duplicates
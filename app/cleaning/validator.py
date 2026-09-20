def find_missing_values(data):

    missing_values = []

    for index, record in enumerate(data, start=2):
        for column, value in record.items():
            if value is None or value == "":
                missing_values.append({
                    "row": index,
                    "column": column
                })

    return missing_values
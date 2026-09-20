def filter_by_value(data, column, value):

    filtered_data = []

    for record in data:
        if record.get(column) == value:
            filtered_data.append(record)

    return filtered_data

def filter_by_condition(data, column, condition):

    filtered_data = []

    for record in data:
        if condition(record.get(column)):
            filtered_data.append(record)

    return filtered_data
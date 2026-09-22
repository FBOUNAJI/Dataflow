def calculate_average(data, column):

    values = []

    for record in data:
        value = record.get(column)

        if isinstance(value, (int, float)):
            values.append(value)

    if not values:
        return 0

    return sum(values) / len(values)

def calculate_minimum(data, column):
  
    values = []

    for record in data:
        value = record.get(column)

        if isinstance(value, (int, float)):
            values.append(value)

    if not values:
        return 0

    return min(values)


def calculate_maximum(data, column):
 
    values = []

    for record in data:
        value = record.get(column)

        if isinstance(value, (int, float)):
            values.append(value)

    if not values:
        return 0

    return max(values)

def calculate_total(data, column):
   
    values = []

    for record in data:
        value = record.get(column)

        if isinstance(value, (int, float)):
            values.append(value)

    return sum(values)

def generate_statistics(data, column):
  
    return {
        "average": calculate_average(data, column),
        "minimum": calculate_minimum(data, column),
        "maximum": calculate_maximum(data, column),
        "total": calculate_total(data, column)
    }
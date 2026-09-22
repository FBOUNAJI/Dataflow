def calculate_department_averages(data, department_column, value_column):
   
    department_values = {}

    for record in data:
        department = record.get(department_column)
        value = record.get(value_column)

        if department and isinstance(value, (int, float)):
            if department not in department_values:
                department_values[department] = []

            department_values[department].append(value)

    department_averages = {}

    for department, values in department_values.items():
        department_averages[department] = sum(values) / len(values)

    return department_averages
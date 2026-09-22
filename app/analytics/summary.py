def count_records(data):

    return len(data)


def get_departments(data, column="Department"):
  
    departments = set()

    for record in data:
        department = record.get(column)

        if department:
            departments.add(department)

    return sorted(departments)
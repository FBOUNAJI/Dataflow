def clean_text_values(data):

    for record in data:
        for column, value in record.items():
            if isinstance(value, str):
                record[column] = value.strip()

    return data
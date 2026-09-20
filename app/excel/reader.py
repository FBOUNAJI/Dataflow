from openpyxl import load_workbook

def read_excel(file_path):

    workbook = load_workbook(file_path)
    worksheet = workbook.active

    rows = list(worksheet.values)

    headers = rows[0]
    data = []

    for row in rows[1:]:
        record = dict(zip(headers, row))
        data.append(record)

    workbook.close()

    return data
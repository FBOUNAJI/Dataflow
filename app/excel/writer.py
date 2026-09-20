from openpyxl import Workbook

def write_excel(data, file_path):

    workbook = Workbook()
    worksheet = workbook.active

    if not data:
        workbook.save(file_path)
        workbook.close()
        return

    headers = list(data[0].keys())
    worksheet.append(headers)

    for record in data:
        row = [record.get(header) for header in headers]
        worksheet.append(row)

    workbook.save(file_path)
    workbook.close()
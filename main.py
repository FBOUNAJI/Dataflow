from app.excel.reader import read_excel
from app.filtering.filter import filter_by_minimum


file_path = "data/input/employees.xlsx"


data = read_excel(file_path)

high_performance_employees = filter_by_minimum(
    data,
    "Performance",
    80
)

print("Employés ayant une performance supérieure ou égale à 80 :")

for employee in high_performance_employees:
    print(employee)
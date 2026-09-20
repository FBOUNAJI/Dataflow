from app.excel.reader import read_excel
from app.filtering.filter import filter_by_condition

file_path = "data/input/employees.xlsx"

data = read_excel(file_path)

high_salary_employees = filter_by_condition(
    data,
    "Salary",
    lambda salary: salary > 7000
)

print("Employés ayant un salaire supérieur à 7000 :")

for employee in high_salary_employees:
    print(employee)
from app.excel.reader import read_excel
from app.analytics.statistics import generate_statistics
from app.analytics.summary import count_records, get_departments
from app.reports.report import (
    save_statistics_report,
    save_statistics_csv,
    save_department_averages
)
from app.analytics.departments import calculate_department_averages

input_file = "data/input/employees.xlsx"
output_file = "data/output/salary_report.txt"
csv_file = "data/output/salary_statistics.csv"
department_file = "data/output/department_salary.csv"

data = read_excel(input_file)

statistics = generate_statistics(data, "Salary")

total_employees = count_records(data)
departments = get_departments(data)
department_averages = calculate_department_averages(
    data,
    "Department",
    "Salary"
)
save_department_averages(
    department_averages,
    department_file
)
save_statistics_report(
    statistics,
    total_employees,
    departments,
    output_file
)
save_statistics_csv(statistics, csv_file)

print("===== Résumé des employés =====")
print(f"Nombre total d'employés : {total_employees}")
print(f"Nombre de départements : {len(departments)}")
print(f"Départements : {', '.join(departments)}")

print("\n===== Salaire moyen par département =====")
for department, average in department_averages.items():
    print(f"{department} : {average:.2f}")

print("\nAnalyse terminée avec succès !")
print(f"Rapport créé : {output_file}")
print(f"Fichier CSV créé : {csv_file}")
print(f"Fichier des salaires par département créé : {department_file}")
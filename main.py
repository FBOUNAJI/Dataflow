from app.excel.reader import read_excel
from app.cleaning.pipeline import clean_data
from app.analytics.statistics import (
    calculate_average,
    calculate_minimum,
    calculate_maximum,
    calculate_total
)
from app.analytics.summary import count_records, get_departments
from app.analytics.departments import calculate_department_averages
from app.reports.report import (
    save_statistics_report,
    save_statistics_csv,
    save_department_averages
)
from app.visualization.charts import create_department_salary_chart
from app.filtering.filter import filter_by_minimum

def main():
    # Input file
    file_path = "data/input/employees.xlsx"

    # Output files
    report_file = "data/output/salary_report.txt"
    csv_file = "data/output/salary_statistics.csv"
    department_file = "data/output/department_salary.csv"
    chart_file = "data/output/department_salary.png"

    # Read Excel data
    data = read_excel(file_path)

    # Clean data
    data, missing_values, cleaning_summary = clean_data(data)

    print("\n===== Data Cleaning =====")
    print(
    f"Records before cleaning : "
    f"{cleaning_summary['records_before']}"
    )
    print(
    f"Records after cleaning  : "
    f"{cleaning_summary['records_after']}"
   )
    print(
    f"Duplicates removed      : "
    f"{cleaning_summary['duplicates_removed']}"
  )
    print(
    f"Missing values found    : "
    f"{cleaning_summary['missing_values']}"
  )

    # Display missing values
    if missing_values:
        print("\n===== Valeurs manquantes =====")

        for item in missing_values:
            print(
                f"Ligne {item['row']} - "
                f"Colonne : {item['column']}"
            )
    else:
        print("\nAucune valeur manquante détectée.")

    # General statistics
    average_salary = calculate_average(data, "Salary")
    minimum_salary = calculate_minimum(data, "Salary")
    maximum_salary = calculate_maximum(data, "Salary")
    total_salary = calculate_total(data, "Salary")

    statistics = {
        "average": average_salary,
        "minimum": minimum_salary,
        "maximum": maximum_salary,
        "total": total_salary
    }

    # Employee summary
    total_employees = count_records(data)
    departments = get_departments(data)

    print("\n===== Résumé des employés =====")
    print(f"Nombre total d'employés : {total_employees}")
    print(f"Nombre de départements : {len(departments)}")
    print(f"Départements : {', '.join(departments)}")

    # Average salary by department
    department_averages = calculate_department_averages(
        data,
        "Department",
        "Salary"
    )

    print("\n===== Salaire moyen par département =====")

    for department, average in department_averages.items():
        print(f"{department} : {average:.2f}")

    # Filter employees by minimum salary
    high_salary_employees = filter_by_minimum(
    data,
    "Salary",
    7000
)

    print("\n===== Employés avec salaire >= 7000 =====")

    for employee in high_salary_employees:
      print(
        f"{employee['Name']} - "
        f"{employee['Department']} - "
        f"{employee['Salary']}"
    )

    # Save reports
    save_statistics_report(
    statistics,
    total_employees,
    departments,
    cleaning_summary,
    high_salary_employees,
    report_file
)

    save_statistics_csv(
        statistics,
        csv_file
    )

    save_department_averages(
        department_averages,
        department_file
    )

    # Create visualization
    create_department_salary_chart(
        department_averages,
        chart_file
    )

    print("\nAnalyse terminée avec succès !")
    print(f"Rapport créé : {report_file}")
    print(f"Fichier CSV créé : {csv_file}")
    print(
        f"Fichier des salaires par département créé : "
        f"{department_file}"
    )
    print(f"Graphique créé : {chart_file}")


if __name__ == "__main__":
    main()
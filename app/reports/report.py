import csv

def save_statistics_report(
    statistics,
    total_employees,
    departments,
    cleaning_summary,
    high_salary_employees,
    file_path
):

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("===== DATAFLOW ANALYSIS REPORT =====\n\n")

        file.write("===== Data Cleaning =====\n")
        file.write(
            f"Records before cleaning : "
            f"{cleaning_summary['records_before']}\n"
        )
        file.write(
            f"Records after cleaning  : "
            f"{cleaning_summary['records_after']}\n"
        )
        file.write(
            f"Duplicates removed      : "
            f"{cleaning_summary['duplicates_removed']}\n"
        )
        file.write(
            f"Missing values found    : "
            f"{cleaning_summary['missing_values']}\n"
        )

        file.write("\n===== Employee Summary =====\n")
        file.write(
            f"Total employees : {total_employees}\n"
        )
        file.write(
            f"Number of departments : {len(departments)}\n"
        )
        file.write(
            f"Departments : {', '.join(departments)}\n"
        )

        file.write("\n===== Salary Analysis =====\n")
        file.write(
            f"Average salary : "
            f"{statistics['average']:.2f}\n"
        )
        file.write(
            f"Minimum salary : "
            f"{statistics['minimum']:.2f}\n"
        )
        file.write(
            f"Maximum salary : "
            f"{statistics['maximum']:.2f}\n"
        )
        file.write(
            f"Total salary : "
            f"{statistics['total']:.2f}\n"
        )

        file.write("\n===== Employees with Salary >= 7000 =====\n")

        for employee in high_salary_employees:
            file.write(
                f"{employee['Name']} - "
                f"{employee['Department']} - "
                f"{employee['Salary']}\n"
            )


def save_statistics_csv(statistics, file_path):

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Statistique",
            "Valeur"
        ])

        writer.writerow([
            "Salaire moyen",
            statistics["average"]
        ])

        writer.writerow([
            "Salaire minimum",
            statistics["minimum"]
        ])

        writer.writerow([
            "Salaire maximum",
            statistics["maximum"]
        ])

        writer.writerow([
            "Masse salariale totale",
            statistics["total"]
        ])


def save_department_averages(
    department_averages,
    file_path
):

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Department",
            "Average Salary"
        ])

        for department, average in department_averages.items():
            writer.writerow([
                department,
                average
            ])
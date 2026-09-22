import csv

def save_statistics_report(statistics, total_employees, departments, file_path):
  
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("===== Résumé des employés =====\n")
        file.write(f"Nombre total d'employés : {total_employees}\n")
        file.write(f"Nombre de départements : {len(departments)}\n")
        file.write(f"Départements : {', '.join(departments)}\n\n")

        file.write("===== Analyse des salaires =====\n")
        file.write(f"Salaire moyen : {statistics['average']:.2f}\n")
        file.write(f"Salaire minimum : {statistics['minimum']:.2f}\n")
        file.write(f"Salaire maximum : {statistics['maximum']:.2f}\n")
        file.write(f"Masse salariale totale : {statistics['total']:.2f}\n")


def save_statistics_csv(statistics, file_path):

    with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        writer.writerow(["Statistique", "Valeur"])
        writer.writerow(["Salaire moyen", statistics["average"]])
        writer.writerow(["Salaire minimum", statistics["minimum"]])
        writer.writerow(["Salaire maximum", statistics["maximum"]])
        writer.writerow(["Masse salariale totale", statistics["total"]])

def save_department_averages(department_averages, file_path):
   
    with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        writer.writerow(["Department", "Average Salary"])

        for department, average in department_averages.items():
            writer.writerow([department, average])
import matplotlib.pyplot as plt

def create_department_salary_chart(department_averages, file_path):
 
    departments = list(department_averages.keys())
    salaries = list(department_averages.values())

    plt.figure(figsize=(8, 5))

    plt.bar(departments, salaries)

    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Salary")

    plt.tight_layout()

    plt.savefig(file_path)
    plt.close()
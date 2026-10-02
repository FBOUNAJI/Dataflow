import os

from app.excel.reader import read_excel
from app.excel.writer import write_excel

from app.cleaning.pipeline import clean_data

from app.analytics.statistics import (
    calculate_average,
    calculate_minimum,
    calculate_maximum,
    calculate_total
)

from app.analytics.summary import (
    count_records,
    get_departments
)

from app.analytics.departments import (
    calculate_department_averages
)

from app.filtering.filter import (
    filter_by_minimum
)

from app.reports.report import (
    save_statistics_report,
    save_statistics_csv,
    save_department_averages
)

from app.visualization.charts import (
    create_department_salary_chart
)


def process_file(input_file, output_directory):

    # Create output directory if it does not exist
    os.makedirs(output_directory, exist_ok=True)

    # Output files
    cleaned_file = os.path.join(
        output_directory,
        "cleaned_data.xlsx"
    )

    report_file = os.path.join(
        output_directory,
        "salary_report.txt"
    )

    csv_file = os.path.join(
        output_directory,
        "salary_statistics.csv"
    )

    department_file = os.path.join(
        output_directory,
        "department_salary.csv"
    )

    chart_file = os.path.join(
        output_directory,
        "department_salary.png"
    )

    # Read Excel file
    data = read_excel(input_file)

    # Clean data
    data, missing_values, cleaning_summary = clean_data(data)

    # Save cleaned Excel file
    write_excel(
        data,
        cleaned_file
    )

    # Salary statistics
    statistics = {
        "average": calculate_average(data, "Salary"),
        "minimum": calculate_minimum(data, "Salary"),
        "maximum": calculate_maximum(data, "Salary"),
        "total": calculate_total(data, "Salary")
    }

    # Employee summary
    total_employees = count_records(data)
    departments = get_departments(data)

    # Average salary by department
    department_averages = calculate_department_averages(
        data,
        "Department",
        "Salary"
    )

    # Filter employees with salary >= 7000
    high_salary_employees = filter_by_minimum(
        data,
        "Salary",
        7000
    )

    # Generate reports
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

    # Generate chart
    create_department_salary_chart(
        department_averages,
        chart_file
    )

    return {
        "cleaned_file": cleaned_file,
        "report_file": report_file,
        "csv_file": csv_file,
        "department_file": department_file,
        "chart_file": chart_file,
        "cleaning_summary": cleaning_summary,
        "missing_values": missing_values,
        "total_employees": total_employees,
        "departments": departments,
        "statistics": statistics
    }
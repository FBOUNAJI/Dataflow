from app.analytics.departments import calculate_department_averages

def test_calculate_department_averages():
    data = [
        {"Department": "IT", "Salary": 7500},
        {"Department": "IT", "Salary": 8500},
        {"Department": "HR", "Salary": 6000},
        {"Department": "HR", "Salary": 7000}
    ]

    result = calculate_department_averages(
        data,
        "Department",
        "Salary"
    )

    assert result["IT"] == 8000
    assert result["HR"] == 6500
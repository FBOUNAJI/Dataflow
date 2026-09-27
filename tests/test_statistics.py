from app.analytics.statistics import (
    calculate_average,
    calculate_minimum,
    calculate_maximum,
    calculate_total
)

def test_calculate_average():
    data = [
        {"Salary": 7500},
        {"Salary": 6500},
        {"Salary": 6000}
    ]

    result = calculate_average(data, "Salary")

    assert result == 6666.666666666667


def test_calculate_minimum():
    data = [
        {"Salary": 7500},
        {"Salary": 6500},
        {"Salary": 6000}
    ]

    result = calculate_minimum(data, "Salary")

    assert result == 6000


def test_calculate_maximum():
    data = [
        {"Salary": 7500},
        {"Salary": 6500},
        {"Salary": 6000}
    ]

    result = calculate_maximum(data, "Salary")

    assert result == 7500


def test_calculate_total():
    data = [
        {"Salary": 7500},
        {"Salary": 6500},
        {"Salary": 6000}
    ]

    result = calculate_total(data, "Salary")

    assert result == 20000
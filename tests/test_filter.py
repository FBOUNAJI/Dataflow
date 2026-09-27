from app.filtering.filter import (
    filter_by_value,
    filter_by_minimum
)


def test_filter_by_value():
    data = [
        {"Name": "Ahmed", "Department": "IT"},
        {"Name": "Sara", "Department": "HR"},
        {"Name": "Youssef", "Department": "IT"}
    ]

    result = filter_by_value(data, "Department", "IT")

    assert len(result) == 2
    assert result[0]["Name"] == "Ahmed"
    assert result[1]["Name"] == "Youssef"


def test_filter_by_minimum():
    data = [
        {"Name": "Ahmed", "Salary": 7500},
        {"Name": "Sara", "Salary": 6500},
        {"Name": "Omar", "Salary": 6000}
    ]

    result = filter_by_minimum(data, "Salary", 7000)

    assert len(result) == 1
    assert result[0]["Name"] == "Ahmed"
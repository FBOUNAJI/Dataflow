from app.cleaning.validator import find_missing_values

def test_find_missing_values():
    data = [
        {"Name": "Ahmed", "Department": "IT", "Salary": 7500},
        {"Name": "Sara", "Department": "", "Salary": 6500},
        {"Name": "Omar", "Department": "IT", "Salary": None}
    ]

    result = find_missing_values(data)

    assert len(result) == 2
    assert result[0]["row"] == 3
    assert result[0]["column"] == "Department"
    assert result[1]["row"] == 4
    assert result[1]["column"] == "Salary"
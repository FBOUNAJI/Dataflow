from app.cleaning.cleaner import clean_text_values
from app.cleaning.deduplicator import remove_duplicates

def test_clean_text_values():
    data = [
        {"Name": "  Ahmed  ", "Department": " IT "},
        {"Name": " Sara", "Department": "HR"}
    ]

    result = clean_text_values(data)

    assert result[0]["Name"] == "Ahmed"
    assert result[0]["Department"] == "IT"
    assert result[1]["Name"] == "Sara"


def test_remove_duplicates():
    data = [
        {"Name": "Ahmed", "Salary": 7500},
        {"Name": "Sara", "Salary": 6500},
        {"Name": "Ahmed", "Salary": 7500}
    ]

    result = remove_duplicates(data)

    assert len(result) == 2
    assert result[0]["Name"] == "Ahmed"
    assert result[1]["Name"] == "Sara"
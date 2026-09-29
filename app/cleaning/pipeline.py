from app.cleaning.cleaner import clean_text_values
from app.cleaning.validator import find_missing_values
from app.cleaning.deduplicator import remove_duplicates


def clean_data(data):

    records_before = len(data)

    # Clean text values
    data = clean_text_values(data)

    # Remove duplicates
    data_without_duplicates = remove_duplicates(data)

    duplicates_removed = (
        len(data) - len(data_without_duplicates)
    )

    # Find missing values
    missing_values = find_missing_values(
        data_without_duplicates
    )

    records_after = len(data_without_duplicates)

    cleaning_summary = {
        "records_before": records_before,
        "records_after": records_after,
        "duplicates_removed": duplicates_removed,
        "missing_values": len(missing_values)
    }

    return (
        data_without_duplicates,
        missing_values,
        cleaning_summary
    )
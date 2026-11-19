from collections import Counter


def validate_csv(headers: list[str], rows: list[list[str]]) -> list[str]:
    errors: list[str] = []

    if not headers:
        return ["CSV file is empty or has no header"]

    if any(not header.strip() for header in headers):
        errors.append("CSV contains an empty column name")

    duplicates = [name for name, count in Counter(headers).items() if count > 1]

    if duplicates:
        errors.append(f"Duplicate column names: {', '.join(duplicates)}")

    for row_number, row in enumerate(rows, start=2):
        if len(row) != len(headers):
            errors.append(f"Row {row_number}: expected {len(headers)} values, got {len(row)}")

    return errors

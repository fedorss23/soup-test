from csv_inspector.validator import validate_csv


def test_valid_csv():
    headers = ["name", "age"]
    rows = [
        ["Fedor", "19"],
        ["Alex", "20"],
    ]

    assert validate_csv(headers, rows) == []


def test_duplicate_headers():
    headers = ["name", "name"]
    rows = [["Fedor", "Alex"]]

    errors = validate_csv(headers, rows)

    assert any("Duplicate column names" in error for error in errors)


def test_invalid_row_length():
    headers = ["name", "age"]
    rows = [["Fedor"]]

    errors = validate_csv(headers, rows)

    assert any("Row 2" in error for error in errors)

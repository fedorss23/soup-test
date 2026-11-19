from csv_inspector.analyzer import analyze_csv


def test_numeric_analysis():
    headers = ["name", "age"]
    rows = [
        ["Fedor", "19"],
        ["Alex", "20"],
        ["John", "21"],
    ]

    result = analyze_csv(headers, rows)

    assert result["age"]["min"] == 19
    assert result["age"]["max"] == 21
    assert result["age"]["avg"] == 20

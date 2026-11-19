from collections import defaultdict


def analyze_csv(headers: list[str], rows: list[list[str]]) -> dict[str, dict[str, float]]:
    numeric_columns: dict[str, list[float]] = defaultdict(list)

    for row in rows:
        for index, value in enumerate(row):
            if index >= len(headers):
                continue

            try:
                number = float(value)
                numeric_columns[headers[index]].append(number)
            except ValueError:
                continue

    result = {}

    for column, values in numeric_columns.items():
        if not values:
            continue

        result[column] = {
            "min": min(values),
            "max": max(values),
            "avg": sum(values) / len(values),
        }

    return result

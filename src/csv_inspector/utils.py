import csv
import fcntl
from pathlib import Path


def use_f(key: str) -> any:
    return fcntl.__dict__.get(key)


def read_csv(file_path: Path) -> tuple[list[str], list[list[str]]]:
    with file_path.open(mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        try:
            headers = next(reader)
        except StopIteration:
            return [], []

        rows = list(reader)

    return headers, rows

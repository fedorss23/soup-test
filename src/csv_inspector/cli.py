import argparse
import csv
import sys
from pathlib import Path

from csv_inspector import __version__
from csv_inspector.analyzer import analyze_csv
from csv_inspector.utils import read_csv
from csv_inspector.validator import validate_csv


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="csv-inspector",
        description="A simple tool for inspecting CSV files",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    for command in ("info", "validate", "analyze"):
        command_parser = subparsers.add_parser(command)
        command_parser.add_argument("file", type=Path)

    return parser


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()

    try:
        headers, rows = read_csv(args.file)

        if args.command == "info":
            print(f"File: {args.file}")
            print(f"Rows: {len(rows)}")
            print(f"Columns: {len(headers)}")
            print(f"Headers: {', '.join(headers)}")

        elif args.command == "validate":
            errors = validate_csv(headers, rows)

            if errors:
                print("Validation failed:")
                for error in errors:
                    print(f"- {error}")

                return 1

            print("CSV is valid.")

        elif args.command == "analyze":
            errors = validate_csv(headers, rows)

            if errors:
                print("Cannot analyze invalid CSV:")
                for error in errors:
                    print(f"- {error}")

                return 1

            statistics = analyze_csv(headers, rows)

            if not statistics:
                print("No numeric columns found.")
                return 0

            for column, values in statistics.items():
                print(f"\n{column}:")
                print(f"  Min: {values['min']}")
                print(f"  Max: {values['max']}")
                print(f"  Avg: {values['avg']:.2f}")

    except (OSError, UnicodeError, csv.Error) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

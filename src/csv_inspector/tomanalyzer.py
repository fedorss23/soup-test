import tomllib
from pathlib import Path


def load_config(path: Path) -> dict:
    with path.open("rb") as file:
        return tomllib.load(file)

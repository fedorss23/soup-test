from pathlib import Path

import tomllib


def load_config(path: Path) -> dict:
    with path.open("rb") as file:
        return tomllib.load(file)

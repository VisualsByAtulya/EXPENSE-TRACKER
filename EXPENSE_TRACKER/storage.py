"""Code for saving and loading the expense data."""


import json
from pathlib import Path


# The JSON file is kept in the same folder as the program.
DATA_FILE = Path("expenses.json")


def load_data():
    if not DATA_FILE.exists():
        return {"expenses": [], "budget": 0}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read the data file. Starting with empty data.")
        return {"expenses": [], "budget": 0}


def save_data(data):
    # indent=4 keeps the JSON file readable when opened manually.
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

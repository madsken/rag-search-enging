import json
import string
import os

SEARCH_LIMT = 5

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")


def load_movies() -> list[dict]:
    return load_data()["movies"]


def load_data() -> dict:
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data


def remove_punctuation(input: str) -> str:
    return input.translate(str.maketrans("", "", string.punctuation))


def tokenize_text(input: str) -> list[str]:
    return input.split()


if __name__ == "__main__":
    print(tokenize_text("h  ey he  las "))

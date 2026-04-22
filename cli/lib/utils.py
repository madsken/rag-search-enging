import json
import string
import os
from nltk.stem import PorterStemmer

SEARCH_LIMT = 5

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")
STOPWORD_PATH = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")


def load_movies() -> list[dict]:
    return load_data()["movies"]


def load_data() -> dict:
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data


def load_stopwords() -> list[str]:
    with open(STOPWORD_PATH, "r") as f:
        words = f.read().splitlines()
    return words


def remove_punctuation(input: str) -> str:
    return input.translate(str.maketrans("", "", string.punctuation))


def tokenize_text(input: str) -> list[str]:
    tokens = input.split()
    cleaned_tokens = []
    for token in tokens:
        if token:
            cleaned_tokens.append(token)

    return cleaned_tokens


if __name__ == "__main__":
    print(tokenize_text("h  ey he  las "))


def stem_tokens(tokens: list[str]) -> list[str]:
    stemmer = PorterStemmer()
    stemmed_tokens = []
    for token in tokens:
        stemmed_tokens.append(stemmer.stem(token))
    return stemmed_tokens

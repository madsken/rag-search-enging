from collections import Counter
from nltk import defaultdict
from .utils import load_movies, CACHE_DIR, tokenize
import pickle
import os


class InvertedIndex:
    def __init__(self) -> None:
        self.index = defaultdict(set)  # dict[token, Set(doc_ids)]
        self.docmap: dict[int, dict] = {}  # dict[doc_id, Docs]
        self.term_frequency: dict[int, Counter] = defaultdict(
            Counter
        )  # dict[doc_id, Counter()]

        self.index_path = os.path.join(CACHE_DIR, "index.pkl")
        self.docmap_path = os.path.join(CACHE_DIR, "docmap.pkl")
        self.term_frequency_path = os.path.join(CACHE_DIR, "term_frequencies.pkl")

    def __add_document(self, doc_id: int, text: str):
        tokens = tokenize(text)
        for token in set(tokens):
            self.index[token].add(doc_id)
            self.term_frequency[doc_id].update(token)

    def get_documents(self, term: str) -> list[int]:
        doc_ids = self.index[term.lower()]
        return sorted(list(doc_ids))

    def build(self):
        movies = load_movies()
        progress = 0
        for movie in movies:
            id = movie["id"]
            text = f"{movie['title']} {movie['description']}"
            self.__add_document(id, text)
            self.docmap[movie["id"]] = movie
            progress += 1
            print(f"Progress: {progress}/{len(movies)}")

    def save(self):
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(self.index_path, "wb") as f:
            pickle.dump(self.index, f)
        with open(self.docmap_path, "wb") as f:
            pickle.dump(self.docmap, f)
        with open(self.term_frequency_path, "wb") as f:
            pickle.dump(self.term_frequency, f)

    def load(self):
        if os.path.exists(self.index_path) and os.path.exists(self.docmap_path):
            with open(self.index_path, "rb") as f:
                self.index = pickle.load(f)
            with open(self.docmap_path, "rb") as f:
                self.docmap = pickle.load(f)
            with open(self.term_frequency_path, "rb") as f:
                self.term_frequency = pickle.load(f)
        else:
            raise FileNotFoundError


def build_command():
    inv_idx = InvertedIndex()
    inv_idx.build()
    inv_idx.save()

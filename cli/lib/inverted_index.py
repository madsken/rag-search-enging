from nltk import defaultdict
from .keyword_search import tokenize
from .utils import load_movies, CACHE_DIR
import pickle
import os


class InvertedIndex:
    def __init__(self) -> None:
        self.index = defaultdict(set)
        self.docmap: dict[int, dict] = {}
        self.index_path = os.path.join(CACHE_DIR, "index.pkl")
        self.docmap_path = os.path.join(CACHE_DIR, "docmap.pkl")

    def __add_document(self, doc_id: int, text: str):
        tokens = tokenize(text)
        for token in set(tokens):
            self.index[token].add(doc_id)

    def get_documents(self, term: str) -> list[int]:
        doc_ids = self.index[term.lower()]
        return sorted(list(doc_ids))

    def build(self):
        movies = load_movies()
        for movie in movies:
            id = movie["id"]
            text = f"{movie['title']} {movie['description']}"
            self.__add_document(id, text)
            self.docmap[movie["id"]] = movie

    def save(self):
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(self.index_path, "wb") as f:
            pickle.dump(self.index, f)
        with open(self.docmap_path, "wb") as f:
            pickle.dump(self.docmap, f)


def build_command():
    inv_idx = InvertedIndex()
    inv_idx.build()
    inv_idx.save()
    docs = inv_idx.get_documents("merida")
    print(f"First document for token 'merida' = {docs[0]}")

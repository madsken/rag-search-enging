from cli.lib.keyword_search import tokenize
from cli.lib.utils import load_movies


class InvertedIndex:
    def __init__(self) -> None:
        self.index = {}
        self.docmap = {}

    def __add_document(self, doc_id: int, text: str):
        tokens = tokenize(text)
        for token in tokens:
            if not self.index[token]:
                self.index[token] = {doc_id}
            else:
                self.index[token].add(doc_id)

    def get_documents(self, term: str) -> list[int]:
        doc_ids = self.index[term.lower()]
        return sorted(list(doc_ids))

    def build(self):
        movies = load_movies()

        pass

    def save(self):
        pass

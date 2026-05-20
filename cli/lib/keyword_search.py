from lib.inverted_index import InvertedIndex
from .utils import (
    SEARCH_LIMT,
    tokenize,
)


def search_command(query: str, limit: int = SEARCH_LIMT) -> list[dict]:
    matches = []
    movie_db = InvertedIndex()
    try:
        movie_db.load()
    except FileNotFoundError as e:
        print(f"Error: File not found\n{e}")
        return matches

    query_tokens = tokenize(query)

    seen = set()
    for tok in query_tokens:
        ids = movie_db.get_documents(tok)
        for id in ids:
            if id in seen:
                continue
            seen.add(id)
            matches.append(movie_db.docmap[id])
            if len(matches) >= limit:
                return matches

    return matches


def has_matching_token(q_toks: list[str], title_toks: list[str]) -> bool:
    for q_tok in q_toks:
        for title_tok in title_toks:
            if q_tok in title_tok:
                return True
    return False

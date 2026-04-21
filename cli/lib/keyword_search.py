from .utils import SEARCH_LIMT, load_movies, remove_punctuation, tokenize_text


def search_command(query: str, limit: int = SEARCH_LIMT) -> list[dict]:
    movies = load_movies()
    matches = []

    query_tokens = preprocess_text(query)

    for movie in movies:
        title_tokens = preprocess_text(movie["title"])

        if has_matching_token(query_tokens, title_tokens):
            matches.append(movie)
            if len(matches) >= limit:
                break

    return matches


def has_matching_token(q_toks: list[str], title_toks: list[str]) -> bool:
    for q_tok in q_toks:
        for title_tok in title_toks:
            if q_tok in title_tok:
                return True
    return False


def preprocess_text(text: str) -> list[str]:
    text = text.lower()
    text = remove_punctuation(text)
    tokens = tokenize_text(text)
    return tokens

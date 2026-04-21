from .utils import SEARCH_LIMT, load_movies, remove_punctuation


def search_command(query: str, limit: int = SEARCH_LIMT) -> list[dict]:
    movies = load_movies()
    matches = []

    query = preprocess_text(query)

    for movie in movies:
        title = preprocess_text(movie["title"])
        if query in title:
            matches.append(movie)
            if len(matches) >= limit:
                break

    return matches


def preprocess_text(text: str) -> str:
    text = text.lower()
    text = remove_punctuation(text)
    return text

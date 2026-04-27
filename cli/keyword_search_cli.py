import argparse
from lib.keyword_search import search_command
from lib.inverted_index import build_command


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("build", help="Buid the inverted index")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "build":
            print("Building inverted index")
            build_command()
            print("Inverted index built successfully.")
        case "search":
            print(f"Searching for: {args.query}")
            matches = search_command(args.query)
            for i, match in enumerate(matches, 1):
                print(f"{i}. ({match['id']}) {match['title']}")
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()

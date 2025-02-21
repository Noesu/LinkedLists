import sys

class BookStudy:
    def __init__(self, name: str, author: str, year: str) -> None:
        self.name = name
        self.author = author
        self.year = int(year)

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other: "BookStudy") -> bool:   # type: ignore[override]
        return all((self.name.lower() == other.name.lower(), self.author.lower() == other.author.lower()))

lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_bs = [BookStudy(*line.split("; ")) for line in lst_in]
unique_books = len(set(lst_bs))

########################################################################################################################

print(unique_books)
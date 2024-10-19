from pricing import NEW_RELEASE, REGULAR, CHILDREN
from dataclasses import dataclass
from typing import Collection


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def get_title(self):
        return self.title

    def is_genre(self, string: str):
        return string.lower() in [g.lower() for g in self.genre]

    def __str__(self):
        return f"{self.title} ({self.year})"

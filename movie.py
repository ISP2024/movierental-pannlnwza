import csv
import logging
from dataclasses import dataclass
from typing import Collection

logging.basicConfig(level=logging.INFO, format='%(message)s')


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


class MovieCatalog:
    _instance = None
    _movies = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls.load_movies('movies.csv')
        return cls._instance

    @classmethod
    def load_movies(cls, path):
        """Load movies from a CSV file and store them in the catalog."""
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for line_number, row in enumerate(reader):
                # skip blank and comment lines
                if not row or row[0].startswith('#'):
                    continue
                if len(row) < 4:
                    logging.warning(f"Line {line_number}: Not enough columns")
                    continue
                try:
                    title = row[1].strip()
                    year = int(row[2].strip())
                    genres = [genre.strip() for genre in row[3].split('|')]
                    movie = Movie(title=title, year=year, genre=genres)
                    cls._movies[title] = movie
                except ValueError:
                    logging.error(f"Line {line_number}: Unrecognized format '{','.join(row)}'")

    def get_movie(self, title, year=None):
        """Retrieve a movie by title and optional year."""
        if year is None:
            return self._movies.get(title)
        else:
            for movie in self._movies.values():
                if movie.title.lower() == title.lower() and movie.year == year:
                    return movie
        return None

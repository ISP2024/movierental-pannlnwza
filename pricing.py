import abc
from datetime import datetime

from movie import Movie


class PriceStrategy(abc.ABC):
    _instance = None

    @abc.abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abc.abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for the rental."""
        pass

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @classmethod
    def price_code_for_movie(cls, movie: Movie):
        """Determine the price code for a given movie."""
        current_year = datetime.now().year
        if movie.year == current_year:
            return NewReleasePrice()
        elif any(genre.lower() in ['children', 'childrens'] for genre in movie.genre):
            return ChildrensPrice()
        else:
            return RegularPrice()


class NewReleasePrice(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_price(self, days: int) -> float:
        return days * 3

    def get_rental_points(self, days: int) -> int:
        return days


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_price(self, days: int) -> float:
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days: int) -> int:
        return 1


class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children's movies."""

    def get_price(self, days: int) -> float:
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days: int) -> int:
        return 1

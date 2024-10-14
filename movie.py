import abc


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


NEW_RELEASE = NewReleasePrice()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = REGULAR
    NEW_RELEASE = NEW_RELEASE
    CHILDRENS = CHILDREN

    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.strategy = price_code

    def get_price_code(self):
        return self.strategy

    def get_title(self):
        return self.title

    def get_price(self, days):
        return self.strategy.get_price(days)

    def get_rental_points(self, days):
        return self.strategy.get_rental_points(days)

    def __str__(self):
        return self.title

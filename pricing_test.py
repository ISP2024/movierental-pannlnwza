import unittest
from pricing import *


class TestPriceCodeForMovie(unittest.TestCase):
    def test_new_release(self):
        movie = Movie("New Release", datetime.now().year, [])
        price_code = PriceStrategy.price_code_for_movie(movie)
        self.assertIsInstance(price_code, NewReleasePrice)

    def test_childrens_movie(self):
        movie = Movie("Childrens Movie", 2020, ["Children"])
        price_code = PriceStrategy.price_code_for_movie(movie)
        self.assertIsInstance(price_code, ChildrensPrice)

    def test_regular_movie(self):
        movie = Movie("Regular Movie", 2019, ["Drama"])
        price_code = PriceStrategy.price_code_for_movie(movie)
        self.assertIsInstance(price_code, RegularPrice)

import unittest
from rental import Rental
from pricing import *


class RentalTest(unittest.TestCase):

	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", 2024, ["Sci-Fi", "Adventure"])
		self.regular_movie = Movie("Air", 2023, ["Drama", "Biography"])
		self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Children"])

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", 2023, ["Drama", "Biography"])
		self.assertEqual("Air", m.get_title())
		self.assertTrue(m.is_genre("Drama"))
		self.assertTrue(m.is_genre("Biography"))
		self.assertFalse(m.is_genre("Sci-Fi"))

	def test_rental_price(self):
		# NEW_RELEASE
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15)
		# REGULAR
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_price(), 2)
		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.get_price(), 3.5)
		# CHILDREN
		rental = Rental(self.childrens_movie, 2)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 4)
		self.assertEqual(rental.get_price(), 3)

	def test_rental_points(self):
		# REGULAR
		rental = Rental(self.regular_movie, 10)
		self.assertEqual(rental.get_rental_points(), 1)
		# CHILDREN
		rental = Rental(self.regular_movie, 14)
		self.assertEqual(rental.get_rental_points(), 1)
		# NEW_RELEASE
		rental = Rental(self.new_movie, 11)
		self.assertEqual(rental.get_rental_points(), 11)

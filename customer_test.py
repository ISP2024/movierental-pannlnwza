import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie

class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""

	def setUp(self):
		"""Test fixture contains:

		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	@unittest.skip("No convenient way to test")
	def test_billing():
		# no convenient way to test billing since its buried in the statement() method.
		pass

	def test_statement(self):
		stmt = self.c.statement()
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4)) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])

	def test_total_charge(self):
		"""Test the total_charge method."""
		rental1 = Rental(self.new_movie, 6)  # 3 * 6 = 18
		self.c.add_rental(rental1)
		rental2 = Rental(self.regular_movie, 5)  # 2 + (1.5 * (5 - 2)) = 6.5
		self.c.add_rental(rental2)
		rental3 = Rental(self.childrens_movie, 4)  # 1.5 + (1.5 * (4 - 3)) = 3
		self.c.add_rental(rental3)
		# 18 + 6.5 + 3 = 27.5
		self.assertEqual(self.c.total_charge(), 27.5)

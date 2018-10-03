# python packages
import unittest

# application
from algorithm_services.algorithms import fizz_buzz
from algorithm_services.algorithms import binnary_search


class FizzBuzzTestCase(unittest.TestCase):

    def tests_should_return_one(self):
        self.assertEqual(fizz_buzz(3)[0], 1)

    def test_should_return_fizz(self):
        self.assertEqual(fizz_buzz(3)[2], 'fizz')

    def test_should_return_buzz(self):
        self.assertEqual(fizz_buzz(5)[4], 'buzz')

    def test_should_return_fizz_buzz(self):
        self.assertEqual(fizz_buzz(15)[14], 'fizz_buzz')

    def test_should_return_number(self):
        self.assertEqual(fizz_buzz(5)[3], 4)


class BinnarySearchTestCase(unittest.TestCase):

    def test_should_return_position_four(self):
        self.assertEqual(binnary_search([2, 9, 13, 34, 55], 55, 0, 4), 4)

    def test_should_find_number_position(self):
        self.assertEqual(binnary_search([2, 3, 6, 9, 13, 16, 55], 55, 0, 6), 6)

    def test_should_not_find_number(self):
        self.assertEqual(binnary_search([1, 4, 7], 5, 0, 2), -1)

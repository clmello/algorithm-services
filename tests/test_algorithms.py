# python packages
import unittest

# application
from algorithm_services.algorithms import fizz_buzz


class AlgorithmsTestCase(unittest.TestCase):

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
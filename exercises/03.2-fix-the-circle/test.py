import unittest
from utils import is_valid_number, validate_numbers
from calculator import add_numbers, multiply_numbers
from validator import validate_calculation

class TestCalculations(unittest.TestCase):
    def test_is_valid_number(self):
        self.assertTrue(is_valid_number(5))
        self.assertTrue(is_valid_number(5.5))
        self.assertFalse(is_valid_number("5"))
        self.assertFalse(is_valid_number(None))

    def test_validate_numbers(self):
        self.assertTrue(validate_numbers(5, 10))
        self.assertTrue(validate_numbers(5.5, 10.5))
        self.assertFalse(validate_numbers(5, "10"))
        self.assertFalse(validate_numbers(None, 10))

    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 10), 15)
        self.assertEqual(add_numbers(5.5, 10.5), 16.0)
        self.assertEqual(add_numbers(5, "10"), "Invalid input")
        self.assertEqual(add_numbers(None, 10), "Invalid input")

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(5, 10), 50)
        self.assertEqual(multiply_numbers(5.5, 10.5), 57.75)
        self.assertEqual(multiply_numbers(5, "10"), "Invalid input")
        self.assertEqual(multiply_numbers(None, 10), "Invalid input")

    def test_validate_calculation(self):
        self.assertTrue(validate_calculation(add_numbers, 5, 10))
        self.assertTrue(validate_calculation(multiply_numbers, 5.5, 10.5))
        self.assertFalse(validate_calculation(add_numbers, 5, "10"))
        self.assertFalse(validate_calculation(multiply_numbers, None, 10))

if __name__ == '__main__':
    unittest.main()
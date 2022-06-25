#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ord_list = [2, 6, 24, 72, 216, 648]
        self.assertEqual(max_integer(ord_list), 648)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unord_list = [10, 200, 17, 89, 40, 3]
        self.assertEqual(max_integer(unord_list), 200)

    def test_max_beginning(self):
        """Test a list with a beginning max value."""
        max_beginning = [100, 33, 4, 1]
        self.assertEqual(max_integer(max_beginning), 100)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [500]
        self.assertEqua(max_integer(one_element), 500)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string"""
        string = "Cars"
        self.assertEqual(max_integer(string), 's')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Cars", "for", "sale", "Eswatini"]
        self.assertEqual(max_integer(strings), "Eswatini")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()

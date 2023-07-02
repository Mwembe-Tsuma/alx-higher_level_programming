#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer(list=[..])."""

    def test_ol(self):
        """Test an ordered list."""
        ol = [1, 2, 3, 4]
        self.assertEqual(max_integer(ol), 4)

    def test_ul(self):
        """Test an unordered list."""
        ul = [1, 2, 4, 3]
        self.assertEqual(max_integer(ul), 4)

    def test_max_at_beg(self):
        """Test a list with max beginning."""
        max_val = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_val), 4)

    def test_empty_l(self):
        """Test an empty list."""
        e_list = []
        self.assertEqual(max_integer(e_list), None)

    def test_one_element(self):
        """Test a list with a one element."""
        one_ele = [6]
        self.assertEqual(max_integer(one_ele), 6)

    def test_float(self):
        """Test a list of floats."""
        float_nums = [1.56, 6.58, -9.133, 16.7, 6.4]
        self.assertEqual(max_integer(float_nums), 16.7)

    def test_int_or_float(self):
        """Test a list of integers and floats."""
        int_or_float = [1.55, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(int_or_float), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Manu"
        self.assertEqual(max_integer(string), 'u')

    def test_list_of_string(self):
        """Test a list of strings."""
        strings = ["Manu", "is", "your", "guy"]
        self.assertEqual(max_integer(strings), "your")

    def test_empty_str(self):
        """Test empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_at_start(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_one_negative(self):
        self.assertEqual(max_integer([1, 2, -3]), 2)

    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()

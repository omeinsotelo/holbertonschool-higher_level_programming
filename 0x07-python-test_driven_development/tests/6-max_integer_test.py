#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def testing_max_integer(self):
        """
        testing with assetEquals the max_integer function
        self: object
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8]), 8)
        self.assertEqual(max_integer([-80, 78, 500, 230]), 500)
        self.assertEqual(max_integer([-3300, 7]), 7)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-3, -10, -9, -20, -8]), -3)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([-7.5, -9.3]), -7.5)
        self.assertEqual(max_integer([2.6, 2.1, 9.4, 1.4]), 9.4)
        self.assertEqual(max_integer([1.1, 1.2, 1.3, float(1)]), float(1.3))
        self.assertEqual(max_integer([1.1, 1, 2.2, 2]), 2.2)
        self.assertEqual(max_integer([3/2, 1, 0.4, 1-0]), 3/2)

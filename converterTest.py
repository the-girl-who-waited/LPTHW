import unittest
from converter import *


class converterTest(unittest.TestCase):

    def test_addTwoThings0(self):
        result = addTwoThings(5, 2)
        self.assertEqual(7, result)

    def test_addTwoThings1(self):
        result = addTwoThings(-5, 2)
        self.assertEqual(-3, result)

    def test_addTwoThings2(self):
        result = addTwoThings(0, 1)
        self.assertEqual(1, result)

    def test_multiplyTwoThings0(self):
        result = multiplyTwoThings(5, 2)
        self.assertEqual(10, result)

    def test_multiplyTwoThings1(self):
        result = multiplyTwoThings(-5, -2)
        self.assertEqual(10, result)



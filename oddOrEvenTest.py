import unittest
from oddOrEven import *


class oddOrEvenTest(unittest.TestCase):
# unresolved referance = refering to something not there
    def test_oddOrEven(self):
        result = oddOrEven(5)
        self.assertEqual("odd", result)

    def test_oddOrEven0(self):
        result = oddOrEven(8)
        self.assertEqual("even", result)

    def test_oddOrEven1(self):
        result = oddOrEven(0)
        self.assertEqual("NA", result)

    def test_oddOrEven2(self):
        result = oddOrEven("5")
        self.assertEqual("NAN", result)

    def test_oddOrEven3(self):
        result = oddOrEven(7)
        self.assertEqual("odd", result)

    def test_mathboy(self):
        result = mathboy(7, 2)
        self.assertEqual(5, result)

    def test_mathboy1(self):
        result = mathboy(13, 7)
        self.assertEqual(6, result)

    def test_mathboy2(self):
            result = mathboy(10, 7)
            self.assertEqual(3, result)



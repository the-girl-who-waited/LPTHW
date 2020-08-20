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

    def test_mathBoyAdd(self):
        result = mathBoyAdd(7, 2)
        self.assertEqual(9, result)

    def test_mathBoyAdd1(self):
        result = mathBoyAdd(13, 7)
        self.assertEqual(20, result)

    def test_mathBoyAdd2(self):
        result = mathBoyAdd(10, 7)
        self.assertEqual(17, result)

    def test_mathBoySubtract(self):
        result = mathBoySubtract(10, 7)
        self.assertEqual(3, result)

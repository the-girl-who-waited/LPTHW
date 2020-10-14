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

    def test_isEven(self):
        result = isEven(2)
        self.assertEqual(result, True)

    def test_isEven0(self):
        result = isEven(3)
        self.assertEqual(result, None)

    def test_fbLite(self):
        result = fbLite(9)
        self.assertEqual(result, "fizz")

    def test_fblite1(self):
        result = fbLite(4)
        self.assertEqual(result, 'buzz')

    def test_lengthCheck(self):
        result = lengthCheck("cake")
        self.assertEqual(result, 'joe')

    def test_lengthCheck1(self):
        result = lengthCheck("cakes")
        self.assertEqual(result, 'jerk')

    def test_lengthCheck2(self):
        result = lengthCheck("")
        self.assertEqual(result, "neither")

    def test_characterFrequency(self):
        result = characterFrequency("asapam", "a")
        self.assertEqual(result, 3)

    def test_returnIndex(self):
        arrayToCheck = ["things", "stuff", "men", "broads"]
        result = returnIndex(arrayToCheck, 0)  # "things"
        self.assertEqual(result, "things")

    def test_reorderArray0(self):
        arrayToCheck = [10, 238, 5, 9, 39]
        result = reorderArray(arrayToCheck, "asc")
        self.assertEqual(result, [5, 9, 10, 39, 238])

    def test_reorderArray1(self):
        arrayToCheck = [10, 238, 5, 9, 39]
        result = reorderArray(arrayToCheck, "desc")
        self.assertEqual([238, 39, 10, 9, 5], result)  # thing, and then result

    def test_reorderArray2(self):
        arrayToCheck = ["b", "o", "o", "b", "s"]
        result = reorderArray(arrayToCheck, "asc")
        self.assertEqual(["b", "b", "o", "o", "s"], result)

    def test_reorderArray3(self):
        arrayToCheck = ["j", "e", "r", "k"]
        result = reorderArray(arrayToCheck, "desc")
        self.assertEqual(["r", "k", "j", "e"], result)

    def test_reorderLength(self):
        arrayToCheck = ["a", "schmo", "dingle", "waterCloset"]  # arrays MUST BE homogenous
        result = reorderLength(arrayToCheck, "desc")
        self.assertEqual(["waterCloset", "dingle", "schmo", "a"], result)

    def test_reorderArray4(self):
        arrayToCheck = [["a"], ["x"], ["n"]]
        result = reorderArray(arrayToCheck, "asc")
        self.assertEqual([["a"], ["n"], ["x"]], result)

    def test_doubleOrder(self):
        arrayToCheck = [["n", "x", "b"], ["y", "d", "c"], ["z", "g", "e"]]
        result = doubleOrder(arrayToCheck, "asc")
        self.assertEqual([["b", "n", "x"], ["c", "d", "y"], ["e", "g", "z"]], result)

    def test_doubleOrder1(self):
        arrayToCheck = [["n", "x", "b"], ["y", "d", "c"], ["z", "g", "e"]]
        result = doubleOrder(arrayToCheck, "desc")
        self.assertEqual([["e", "g", "z"], ["c", "d", "y"], ["b", "n", "x"]], result)

    def test_addTwo(self):
        arrayToCheck = [1, 2, 3, 4, 5]
        result = addTwo(arrayToCheck)
        self.assertEqual([3, 4, 5, 6, 7], result)

    def test_smallAndLarge(self):
        arrayToCheck = [3, 5, 1, 4, 2, 10]
        result = smallAndLarge(arrayToCheck)
        self.assertEqual([1, 10], result)

    def test_removeSpaces(self):
        spaced = "thirty five times"
        result = removeSpaces(spaced)
        self.assertEqual("thirtyfivetimes", result)

    def test_splitArray(self):
        toSplit = [1, 2, 3, 4, 5, 6] # [4, 5, 6]
        result = splitArray(toSplit)
        self.assertEqual([[1, 2, 3], [4, 5, 6]], result)

    def test_evenChars(self):
        result = evenChars("junk")
        self.assertEqual(True, result)

    def test_evenCharsOdd(self):
        result = evenChars("3junk")
        self.assertEqual(None, result)

    def test_truthy(self):
        even = "junk"
        result = truthy(even)
        self.assertEqual("it's even", result)

    def test_truthyNone(self):
        even = "odd3"
        result = truthy(even)
        self.assertEqual("it's even", result)

    def test_truthyOdd(self):
        even = "odd"
        result = truthy(even)
        self.assertEqual("meh", result)

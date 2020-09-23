# functions need four things
# 0. a GOOD NAME
# 1. parenthesis that contain parameters with good names(number0, number1)
# 2. a body (what does the function DO when you call it)
# 3. a call to activate it

def oddOrEven(number):
    if isinstance(number, str):
        return "NAN"
    elif number == 0:
        return "NA"
    elif number % 2 == 0:
        return "even"
    else:
        return "odd"


# elif will only be read if the previous conditional reads false

def mathBoyAdd(number0, number1):
    return number0 + number1


def mathBoySubtract(number0, number1):
    return number0 - number1


def fbLite(number):
    if oddOrEven(number) == "odd":
        return "fizz"
    elif oddOrEven(number) == "even":
        return "buzz"
    elif oddOrEven(number) == "NAN":
        return oddOrEven(number)


def lengthCheck(stringToCheck):  # we give the function a name and a perameter
    length = len(str(stringToCheck))  # we run str on input then we run len then we assign a var name

    decided = oddOrEven(length)  # defining a variable by calling oddOrEven(length)
    if decided == "even":  # if oddOrEven returns "even"
        return "joe"
    elif decided == "odd":
        return "jerk"
    else:
        return "neither"


def characterFrequency(string, char):
    return string.count(char)  # native function count can only take strings


def returnIndex(array, idxToCheck):
    return array[idxToCheck]


def reorderArray(array, order):
    if order == "asc":
        return sorted(array)
    elif order == "desc":
        return sorted(array, reverse=True)


def reorderLength(array, order):
    if order == "asc":
        return sorted(array, key=len)
    elif order == "desc":
        return sorted(array, key=len, reverse=True)


def doubleOrder(arrayOfArrays, order): # gave the function a name and gave it two arguments
    orderedArray = [] # defined a variable with an empty array
    for subArray in arrayOfArrays: # has the function look at one small section of the array
        orderedArray.append(sorted(subArray))
    # tells the function to put a small section of the array back into the larger array in the given order
    if order == "asc": # if the order given in the variable is ascending then do something
        return sorted(orderedArray) # return an array sorted in ascending order
    elif order == "desc": # if the variable does not say ascending, its descending do something
        return sorted(orderedArray, reverse=True) # return an array ordered in the reverse of ascending order


def addTwo(arrayOfInts):
    newArray = []
    for integer in arrayOfInts:
        newArray.append(integer + 2)
    return newArray


def findLargest(arrayOfInts):
    return sorted(arrayOfInts)[-1]


def removeSpaces(string):
    nuString = ""
    for char in string:
        if char != " ":
            nuString += char # nuString = nuString + string[char]
            print(nuString)
    return nuString


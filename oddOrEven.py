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
    else :
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

def lengthCheck(input): # we give the function a name and a perameter
    length = len(str(input)) #we run str on input then we run len then we assign a var name
    
    decided = oddOrEven(length) #  defining a variable by calling oddOrEven(length)
    if decided == "even": # if oddOrEven returns "even"
        return "joe"
    elif decided == "odd":
        return "jerk"
    else:
        return "neither"

def characterFrequency(string, char):
    return string.count(char)


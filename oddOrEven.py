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

def mathboy(number0, number1):
    return number0 + number1

def mathboy(number0, number1):
    return number0 - number1
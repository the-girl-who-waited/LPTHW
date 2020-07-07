num = 3

if 3 >= 0:
    print("positive or zero")
else:
    print("negative number")

num = -5

if -5 >= 0:
    print("positive or zero")
else:
    print("negative number")


# i want a function that tells if a number is greater than 0

def zeroOrHigher(number):
    if number >= 0:
        print("true")
    else:
        print("false")

zeroOrHigher(5)
zeroOrHigher(0)




# functions need four things
# 0. a GOOD NAME
# 1. parenthesis that contain parameters with good names(number0, number1)
# 2. a body (what does the function DO when you call it)
# 3. a call to activate it

# sumOfThree(238, 1)

# i want this to add two strings
def concatTwoStrings(string0, string1):
    print(string0 + " " + string1)


concatTwoStrings("8", "238")


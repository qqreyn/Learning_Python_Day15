import math

def calculator (x, y, operation):
    if operation == 1:
        return x + y
    elif operation == 2:
        return x - y
    elif operation == 3:
        return x * y
    elif operation == 4:
        try:
            return x / y
        except ZeroDivisionError:
            print("You can't divide by 0")
    else:
        print("Incorrect operation, pick from 1-6")

def calculator_adv(x, operation):
    if operation == 5:
        return x ** 2
    elif operation == 6:
        return math.sqrt(x)
    else:
        print("Incorrect operation, pick from 1-6")

def greeting(name):
    print("Welcome,", name, "nice to meet you!")
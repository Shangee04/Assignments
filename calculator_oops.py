def add(number_1, number_2):
    """ Add function is created"""
    return number_1 + number_2


def sub(number_1, number_2):
    """ Sub function is created"""
    return number_1 - number_2


def mul(number_1, number_2):
    """ Mul function is created"""
    return number_1 * number_2


def div(number_1, number_2):
    """ Div function is created"""
    try:
        Result = number_1/number_2
    except ZeroDivisionError as err:
        print('Error',err)
    else:
        print('Result')


def mod(number_1, number_2):
    """ Mod function is created"""
    return number_1 % number_2


class Calculators:
    """class is created"""


if __name__ == "__main__":
    my_cal = Calculators()
    ch = 1
    while ch != 0:
        print("1: Add")
        print("2: Sub")
        print("3: Mul")
        print("4: Div")
        print("5: Mod")
        ch = int(input("select operation: "))
        num3 = int(input("enter the first number: "))
        num4 = int(input("enter the second number: "))
        if ch == 1:
            print("Result: ", add(num3, num4))
        elif ch == 2:
            print("Result: ", sub(num3, num4))
        elif ch == 3:
            print("Result: ", mul(num3, num4))
        elif ch == 4:
            print("Result: ", div(num3, num4))
        elif ch == 5:
            print("Result: ", mod(num3, num4))
        else:
            print("Invalid input")

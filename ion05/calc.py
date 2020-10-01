import math

a = float(input("Enter the first number"))
b = float(input("Enter the second number (Only for basic 4)"))
op = input("Enter the operation : ")


def sum1(num1, num2):
    print(num1 + num2)


def sub(num1, num2):
    print(num1 - num2)


def mul(num1, num2):
    print(num1 * num2)


def div(num1, num2):
    print(num1 / num2)


def qrt(num1):
    print(math.sqrt(num1))


def roundi(num1):
    print(round(num1))


if op == "Add":
    sum1(a, b)
elif op == "Subtract":
    sub(a, b)
elif op == "Multiply":
    mul(a, b)
elif op == "Divide":
    div(a, b)
elif op == "Square Root":
    print(qrt(a))
elif op == "Round Off":
    roundi(a)

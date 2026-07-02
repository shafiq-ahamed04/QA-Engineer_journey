#calculator

def add(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


num1 = int(input('Enter Number 1: '))
num2 = int(input('Enter Number 2: '))

print()
print('Addition:', add(num1, num2))
print('Subtraction:', subtraction(num1, num2))
print('Multiplication:', multiply(num1, num2))
print('Division:', division(num1, num2))


import math


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    return a / b

def exponent_numbers(a,b):
    return math.pow(a,b)

def set1(a):
    a = 1
    return 1

if __name__ == "__main__":
    print("Adding:", add_numbers(2, 4))
    print("Subtracting:", subtract_numbers(9, 2))

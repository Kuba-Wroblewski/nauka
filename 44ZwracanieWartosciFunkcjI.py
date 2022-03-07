#!/usr/bin/python3

"""
    return - zwrócić
    None - nic - false
"""


def pole_prostokata(a, b):
    print(a * b)


# pole_prostokąta(2, 4)

def pole_prostokata(a, b):
    return a * b


pole_prostokataA = pole_prostokata(2, 4)
pole_prostokataB = pole_prostokata(20, 14)


# print(5 * pole_prostokątaA)
# print(5 * pole_prostokątaB)

def dzielenie(a, b):
    if (b == 0):
        return
    print("test")
    return a / b


print(dzielenie(10, 1))

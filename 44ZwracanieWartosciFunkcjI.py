#!/usr/bin/python3

"""
    return - zwrócić
    None - nic - false
"""

def pole_prostokąta(a, b):
    print(a * b)

# pole_prostokąta(2, 4)

def pole_prostokąta(a, b):
    return a * b

pole_prostokątaA = pole_prostokąta(2, 4)
pole_prostokątaB = pole_prostokąta(20, 14)
# print(5 * pole_prostokątaA)
# print(5 * pole_prostokątaB)

def dzielenie(a, b):
    if (b == 0):
        return
    print("test")
    return a / b

print(dzielenie(10, 1))

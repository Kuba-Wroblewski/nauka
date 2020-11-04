#!/usr/bin/python3

import copy

def evil_function(toBeDestoyed):
    print(id(toBeDestoyed))
    toBeDestoyed[0] = 4
    print(toBeDestoyed, "\n")

myList = [1, 3, 45, 92]

print(id(myList))
evil_function(myList[1:3])
evil_function(myList[:])
print(myList)
print(id(myList))


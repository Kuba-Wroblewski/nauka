#!/usr/bin/python3

a = 5
b = 7

if (a < b):
    print("test") # wypisze nam test bo to prawda
if (-464):
    print("test") # wypisze nam test
if (a):
    print("test") # wypisze nam test
if (4664646548650):
    print("test") # wypisze nam test
if ("fdsfs"):
    print("test") # string tez nam wypisze test

a = 0
b = 7

if (a):
    print("test") # tutaj nam nic nie wypisze ponieważ wyjdzie nam "0"

a = 5
b = 7

if (None):
    print("test") # tutaj nam nic nie wypisze ponieważ "None" jak sama nazwa
    # wskazuje jest to nic czyli cos jak zer.
    # jest to pustka dotycząca objektów.

# czyli wszystkie wartości różne od zera (None) dla Pythona to True prawda

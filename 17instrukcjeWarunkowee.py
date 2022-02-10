#!/usr/bin/python3

"""
Instrukcja warunkowa
jeśli (prawda)
to...
jeśli co innego (prawda)
to...
a całkowicie w innym przypadku
to...
"""

wybór = input("* - mnożenie, / - dzielenie, + - dodać, - - odejmować: ")
a = int(input("Podaj wartość dla pierwszej liczby\n"))
b = int(input("Podaj wartość dla drugiej liczby\n"))

if (wybór == "*"):
    print(a * b)
elif (wybór == "/"):
    if (b == 0):
        print("Cholero nie mnóż przez zero")
    else:
        print(a / b)
elif (wybór == "+"):
    print( a + b)
elif (wybór == "-" or "-"):
    print(a - b)
else:
    print("nie wybrałeś żadnego wyboru")
    

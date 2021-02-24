#!/usr/bin/python3

"""
calc.dodaj =  każda nazwa poprzedzona kropką to atrybut - (dodaj)

Na obiektach klasy można przeprowadzić dwa rodzaje operacji: odniesienia do atrybutów i konkretyzację.

"""



import test_pierwszy


class Calculator():

    def __init__(self):
        print("init")
    def __del__(self):
        print("del")


    def dodaj(self, a, b):
        wynik = a + b
        print(wynik)
    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)
        
# calc = Calculator()
# calc2 = Calculator()

# calc.dodaj(5, 5)
# calc2.dodaj(14, 5)

Calculator()
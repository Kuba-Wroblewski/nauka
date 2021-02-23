#!/usr/bin/python3
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
        
calc = Calculator()
calc2 = Calculator()

calc.dodaj(5, 5)
calc2.dodaj(14, 5)


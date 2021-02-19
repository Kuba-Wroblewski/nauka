#!/usr/bin/python3
import test_pierwszy


class Calculator():

    def dodaj(self, a, b):
        wynik = a + b
        print(wynik)
    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)
        
calc = Calculator()
calc.dodaj(5, 5)


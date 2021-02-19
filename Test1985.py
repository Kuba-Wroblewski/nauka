#!/usr/bin/python3

import requests
import json


#gotowa klasa Pojazd

class Pojazd:
    nazwa = ""
    rodzaj = "auto"
    kolor = ""
    wartosc = 100.00
    def opis(self):
        napis_opisu = "%s to %s %s warty %.2f zl." % (self.nazwa, self.kolor, self.rodzaj, self.wartosc)
        return napis_opisu

# Ponizej umiesc swoj kod
def Auto1(Pojazd):
    nazwa = "Ferari"
    kolor = "czerwony"
    rodzaj = "kabriolet"

# Auto1 = Pojazd()



# sprawdzenie kodu
print(Auto1.opis())
# print(Auto2.opis())

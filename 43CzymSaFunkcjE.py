#!/usr/bin/python3

"""
    Funkcja - to blok kodu do którgo mozna odwolac sie
        w kazdej chwili, aby otrzymac pozadany przez nas wynik.

    definition

"""

def wiadomosć_powitalna(imie):
    print("Cześć ",imie,", miło mi powitać Cię w moim programie!")

imiona = ["Arku", "Wiolu", "Bartku"]

for imie in imiona:
    wiadomosć_powitalna(imie)

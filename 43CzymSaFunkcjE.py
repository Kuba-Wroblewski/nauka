#!/usr/bin/python3

"""
    Funkcja - to blok kodu do którgo mozna odwolac sie
        w kazdej chwili, aby otrzymac pożądany przez nas wynik.

    definition

    funkcja pełni fukcje rozwiazujacy problem w jej nazwie.
    (Samoopisująca się) - nazwa funkcji powinna odpowiadała temu co ma zrobić
"""


def wiadomosc_powitalna(imie):
    print("Cześć ", imie, ", miło mi powitać Cię w moim programie!")


imiona = ["Arku", "Wiolu", "Bartku"]

for imie in imiona:
    wiadomosc_powitalna(imie)

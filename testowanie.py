#!/usr/bin/python3

import random
from enum import Enum
Zdarzenie = Enum('Event',['Skrzynia', 'Nic'])
słownikZdarzeń = {Zdarzenie.Skrzynia: 0.6, Zdarzenie.Nic: 0.4}
listaZdarzeń = list(słownikZdarzeń.keys())
prawdopodobneZdarzenia = list(słownikZdarzeń.values())
print("Witaj w mojej grze <LABIRYNT>, Masz tylko 5 ruchów, możesz zdobyć pewną nagrode, lub nie")
Kolor = Enum('Kolory', {'Green': 'zielony', 'Orange': 'pomarańczowy', 'Purple': 'fioletowy', 'Gold': 'złoty'})
skrzyniKolorSłownik = {Kolor.Green :  0.75, Kolor.Orange : 0.2, Kolor.Purple : 0.04, Kolor.Gold : 0.01}
skrzyniKolorLista = tuple(skrzyniKolorSłownik.keys())
skrzyniKolorPrawdopodobieństwo = tuple(skrzyniKolorSłownik.values())
nagrodaZaSkrzynki = {skrzyniKolorLista[reward]: (reward + 1) * (reward + 1) * 1000
                    for reward in range(len(skrzyniKolorSłownik))}

import random
zdobyteZłoto = 0
długość_naszej_gry = 2

while długość_naszej_gry > 0:
    odpowieć_gracza = input("Czy chcesz iść do przodu ?")
    if (odpowieć_gracza == "tak"):
        print("Wspaniale, zobaczmy co zyskałeś...")
        WylosowanyZdarzenie = random.choices(listaZdarzeń, prawdopodobneZdarzenia)[0]
        if (WylosowanyZdarzenie == Zdarzenie.Skrzynia):
            print("Wylosowałeś skrzynke")
            WylosowanaSkrzynia = random.choices(skrzyniKolorLista, skrzyniKolorPrawdopodobieństwo)[0]
            print("Kolor skrzyni jest:", WylosowanaSkrzynia)
            nagrodaGracza = nagrodaZaSkrzynki[WylosowanaSkrzynia]
            zdobyteZłoto += nagrodaGracza
        elif (listaZdarzeń == Zdarzenie.Nic):
            print("Nic nie wylosowałeś masz pecha")
    else:
        print("Możesz iść tylko do przodu im sorry")
        continue

    długość_naszej_gry -= 1
print("Gratulacje zdobyłes", zdobyteZłoto)
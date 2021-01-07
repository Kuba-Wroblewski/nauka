#!/usr/bin/python3

import random
from enum import Enum

Zdarzenie = Enum('Event',['Chest', 'Empty'])

słownikZdarzeń = {Zdarzenie.Skrzynia: 0.6, Zdarzenie.Nic: 0.4}
listaZdarzeń = list(listaZdarzeń.keys())
prawdopodobneZdarzenia = list(listaZdarzeń.values())

print("Witaj w mojej grze <LABIRYNT>, Masz tylko 5 ruchów, możesz zdobyć pewną nagrode, lub nie")

Kolor = Enum('Kolory', {'Green': 'zielony', 'Orange': 'pomarańczowy', 'Purple': 'fioletowy', 'Gold': 'złoty'})
  
chestColoursDictionary = {Kolor.Green :  0.75, Kolor.Orange : 0.2, Kolor.Purple : 0.04, Kolor.Gold : 0.01}

skrzyniKolorLista = tuple(skrzyniKolorLista.keys())
skrzyniKolorPrawdopodobieństwo = tuple(skrzyniKolorPrawdopodobieństwo.values())

rewardsForChests = {skrzyniKolorLista[reward]: (reward + 1) * (reward + 1) * 1000
                    for reward in range(len(skrzyniKolorLista))}

import random

długość_naszej_gry = 5

while długość_naszej_gry > 0:
    odpowieć_gracza = input("Czy chcesz iść do przodu ?")
    if (odpowieć_gracza == "tak"):
        print("Wspaniale, zobaczmy co zyskałeś...")
        random.choices
    else:
        print("Możesz iść tylko do przodu MEAN 'tak'")
        continue

    długość_naszej_gry -= 1



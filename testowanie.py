#!/usr/bin/python3

import random
from enum import Enum
Zdarzenie = Enum('Zdarzenie', ['Skrzynia', 'Nic'])

słownikZdarzeń = { Zdarzenie.Skrzynia: 0.6, Zdarzenie.Nic: 0.4}
zdarzenieLista = list(słownikZdarzeń.keys())
zdarzeniePrawdopodobne = list(słownikZdarzeń.values())

Color = Enum('Color', {'Green': 'Zielony', 'Orange' :'Pomarańczowy',
                    'Purple': 'Fioletowy', 'Gold': 'Złoty'})

słownikColoruSkrzyni = {Color.Green: 0.75, Color.Orange: 0.2,
                        Color.Purple: 0.04, Color.Gold: 0.01}                      
zdarzenieColorLista = list(słownikColoruSkrzyni.keys())
zdarzenieColorPrawdopodobne = list(słownikColoruSkrzyni.values())

nagrodaZaSkrzynki = { zdarzenieColorLista[nagroda]: (nagroda +1) * (nagroda +1) *1000
                        for nagroda in range(len(słownikColoruSkrzyni)) }

długośćGry = 5
złotoZdobyteWgrze = 0

print("""Witaj w mojej grze o nazwie Komnata,
Masz tylko 5 ruchów do przodu, zobacz na koniec gry ile złota zdobędziesz""")

while długośćGry > 0:
    graczOdpowiada = input("Czy chcesz iść do przodu?\n")
    if (graczOdpowiada == "no"):
        print("Wspaniale, zobaczmy co wygrałeś...\n")
        wylosowaneZdarzenie = random.choices(zdarzenieLista, zdarzeniePrawdopodobne)[0]
        if (wylosowaneZdarzenie == Zdarzenie.Skrzynia):
            print("Gratulacje zdobyłeś skrzynie")
            WylosowanieColoruSkrzyni = random.choices(zdarzenieColorLista, zdarzenieColorPrawdopodobne)[0]
            print("Color twojej skrzynki to:", WylosowanieColoruSkrzyni.value)
            nagrodaWgrze = nagrodaZaSkrzynki[WylosowanieColoruSkrzyni]
            złotoZdobyteWgrze = złotoZdobyteWgrze + nagrodaWgrze  
        elif (wylosowaneZdarzenie == Zdarzenie.Nic):
            print("Masz pecha nic nie zdobyłeś")   
    else:
        print("Niestety możesz iśc tylko do przodu prykro nam") 
        continue

    długośćGry -= 1
print("Gratulacje zdobyłes:", złotoZdobyteWgrze)
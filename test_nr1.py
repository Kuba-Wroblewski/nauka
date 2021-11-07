#!/usr/bin/python3
import random
from enum import IntEnum
from enum import Enum


zdarzenie = IntEnum('zdarzenie',('Skrzynia Nic'))
prawdopodobienstwoZdarzenia = {zdarzenie.Skrzynia:0.6, zdarzenie.Nic:0.4}
slownikZdarzen = list(prawdopodobienstwoZdarzenia.keys())
slownikPrawdopodobienstwaZdarzenia = list(prawdopodobienstwoZdarzenia.values())

kolorSkrzyni = Enum('kolor',{'Zielona':'Green', 'Pomaranczowa':'Orange', 'Fioletowa':'Purple', 'Zlota':'Gold'})
prawdopodobienstwoKolorSkrzyni = {kolorSkrzyni.Zielona:0.75, 
                                kolorSkrzyni.Pomaranczowa:0.2, 
                                kolorSkrzyni.Fioletowa:0.04, 
                                kolorSkrzyni.Zlota:0.01}
slownikKolorSkrzyni = list(prawdopodobienstwoKolorSkrzyni.keys())
slownikPrawdopodobienstwoKolorSkrzyni = list(prawdopodobienstwoKolorSkrzyni.values())

zdobyteZlotoZeSkrzyni = {slownikKolorSkrzyni[nagroda]:(nagroda + 1)* (nagroda + 1) * 1000 
                        for nagroda in range(len(slownikKolorSkrzyni))}

def przyblizonaWartoscZlota(zloto):
    nizszaWartosc = zloto - 0.1 * zloto
    wyzszaWartosc = zloto + 0.1 * zloto
    return random.randint(nizszaWartosc, wyzszaWartosc)


print('Witaj. w mojej grze "KOMNATA"')
print('Masz 5 ruchów idąc do przodu przez KOMNATE zobaczymy ile złota zdobędziesz')
zdobyteZlotoWGrze = 0
dlugoscGry = 5
while dlugoscGry > 0:
    odpowiedzGracza = int(input(' Czy chcesz iść prosto przez KOMNATE ? jeśli tak wpisz "1"\n'))
    if odpowiedzGracza == 1:
        print('Zobaczmy czy cos udało ci sie zdobyc')
        zdarzenieGracza = random.choices(slownikZdarzen, slownikPrawdopodobienstwaZdarzenia)[0]
        if zdarzenieGracza == zdarzenie.Skrzynia:
            wylosowanyKolorSkrzyni = random.choices(slownikKolorSkrzyni, slownikPrawdopodobienstwoKolorSkrzyni)[0]
            print('Gratulacje zdobyłeś Skrzynie koloru:', wylosowanyKolorSkrzyni)
            zdobyteZloto = przyblizonaWartoscZlota(zdobyteZlotoZeSkrzyni[wylosowanyKolorSkrzyni])
            print('Zdobyte złoto z wylosowanej skrzyni to:', zdobyteZloto)
            zdobyteZlotoWGrze += zdobyteZloto
        else:
            print('Nie stety nie udało ci się nic zdobyć')
    else:  
        print('W tej grze możesz isc tylko na wprost')
        continue
    dlugoscGry -= 1
if zdobyteZlotoWGrze > 0:
    print('Gratulacje udało ci się zdobyć w tej grze', zdobyteZlotoWGrze, 'złota')
else:
    print('Nie stety nic nie zdobyłeś w całęj grze')
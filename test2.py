#!/usr/bin/python3
import time

# Wyrażenia listowne
# wypisz potęge z listy liczb
'''
Co robić na elemencie
Skąd mamy ten element
warunek oparty na elemencie
'''

liczby = [1,2,3,4,5,6]
names = {'Arkadiusz', 'wioletta', 'karol', 'Kuba', 'Justyna', 'Aniela'}
celcius = {'t1':-20, 't2':-15, 't3':0, 't4':12, 't5':23}

potęgaLiczb = []
for liczba in liczby:
    potęgaLiczb.append(liczba)
print(potęgaLiczb)
potegiDwojki2 = [liczba ** 2
                for liczba in liczby
                ]
print(potegiDwojki2)
# wypisz liczby parzyste z listy liczb
liczbyParzyste = []
for liczba in liczby:
    if liczba %2 == 0:
        liczbyParzyste.append(liczba)
print(liczbyParzyste)
liczbyParzyste = [liczba
                for liczba in liczby
                if liczba %2 == 0
                ]
# Wyrażenie generującego
evenNumbers = (liczba 
                for liczba in liczby
                if liczba %2 ==0
                )
for item in evenNumbers:
    print(item)
# Wyrażenia słownikowe
# 1.pokaż imie wraz z ilością jego liter, pokarz tylko imiona zaczynające sie na litere 'A'
nameLenght = {name:len(name)
            for name in names
            if name.startswith('A')
            }
print(nameLenght)            
# 2. chcemy przenożyć przez siebie kazdą z liczb,
# i jako klucz wartosc podstawowa a jako wartość wartość przemnożoną

multipedNumbers = {liczba:liczba*liczba
                for liczba in liczby
                }
print(multipedNumbers)
# klucze pozostawić te same lecz wartości mają automatycznie sie zmienić z celciusza na farenhajta
# pokaż temperature większa od -5
celciusToFarenh = {celciusz:(celciusz * 1.8) + 32
                for key, celciusz in celcius.items()
                if celciusz > -5
                }
print(celciusToFarenh) 
# wyrazenie zbioru
# Wypisać wszsytkie imiona aby pierwsza litera była z duzej
namesBig = {name.upper()
            for name in names
            }
print(namesBig)
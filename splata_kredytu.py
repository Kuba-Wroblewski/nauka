#!/usr/bin/python3

import time

input('Dzien dobry')

a = input('Jak masz na imię ?...')
print(a+'...')
print('Miło mi Cie poznać')
print('Ja jestem "Misiek" ')
b = input('Czy Tobie też miło, mnie poznać ?...')
if b == 'Tak' or b == 'tak' or b == 'oczywiście' or b == 'Oczywiście' or b == 'Oczywiscie' or b == 'oczywiscie':
    print('Ciesze się')
else:
    print('Przykro mi :(')

print("Policzymy dziś ile potrzebujesz miesięcy na spłatę 10 000 zł.")
print('Od pewnej sumy musimy zacząć nawet jak to jest kwota debetowa ujemna :)')
suma = input('Proszę wprowadzić od jakiej ilości pieniędzy zaczynamy zbiórkę ?....(Proszę wprowadzić liczbę całkowitą)')
print('Dobrze więc zaczynamy zbierać pieniążki od'), print(suma + str('zł'))
time.sleep(1)
suma = int(suma)

while True:
    print('Proszę wpisać pieniądze odłożone co miesiąc po wpisaniu sumy kliknąć "ENTER" i czynoość powtarzamy...')
    x = input()
    suma += int(x)
    print(suma)
    if suma >= 10000:
        print('Udało się mamy to !!!')

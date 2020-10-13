#!/usr/bin/python3

"""
napisz program ktory policzy sumę liczb od 1 do podanej liczby przez uzytkownika
<<<<<<< HEAD
=======

>>>>>>> c7f9ed5b78ea961bab424488734a5665cb719de7
dla np.5
1+2+3+4+5
zwroci
15
"""
import time
#
# def suma_liczby():
#     wybór = int(input("Podaj jakąś liczbę całkowitą...\n"))
#     evenNumbers = [element for element in range(1, wybór +1)]
#     return sum(evenNumbers)
# print(suma_liczby())

def suma_liczby(liczba):
    suma = 0
    for liczba in range(1, liczba + 1):
        suma = suma + liczba
    return suma

def suma_liczby1(liczba):
    wynik = []
    for element in range(1, liczba + 1):
        wynik.append(element)
    return sum(wynik)

# Lista wyrażeniowa
def suma_liczby2(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])
# Set zbiór
def suma_liczby3(liczba):
    return sum({liczba for liczba in range(1, liczba + 1)})
# Generator
def suma_liczby4(liczba):
    return sum((liczba for liczba in range(1, liczba + 1)))
# Wyrażenie arytmetyczne
def suma_liczby5(liczba):
    return (1 + liczba) / 2 * liczba

def finish_timer(start):
    koniec = time.perf_counter()
    return koniec - start

start = time.perf_counter()
print(suma_liczby(5000000))
print("PIERWSZY", finish_timer(start))

start = time.perf_counter()
print(suma_liczby1(5000000))
print("PIERWSZY 2", finish_timer(start))

start = time.perf_counter()
print(suma_liczby2(5000000))
print("DRUGI", finish_timer(start))

start = time.perf_counter()
print(suma_liczby3(5000000))
print("TRZECI", finish_timer(start))

start = time.perf_counter()
print(suma_liczby4(5000000))
print("CZWARTY", finish_timer(start))

start = time.perf_counter()
print(suma_liczby5(5000000))
print("PIĄTY", finish_timer(start))



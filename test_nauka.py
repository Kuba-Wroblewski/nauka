#!/usr/bin/python3


"""
    Ćwiczenie
    Napisz program, który obliczy sumę wszystkich liczb
    od 1 do podanej podanej liczby przez użytkownika

    np. dla 5
    1+2+3+4+5 = 15
    zwróci 15

"""
import time

def suma_liczby(liczba):
    suma = 0

    for liczba in range(1, liczba + 1):
        suma = suma + liczba
    return suma
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

def function_performance(func, arg, how_many_times=20):
    suma = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        suma += (end - start)
    return suma

def function_performance1(func, arg, how_many_times=5):
    suma = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        suma = suma + (end - start)
    return suma

def show_message(message):
    print(message)

# print(function_performance(suma_liczby, 500000, ))
print(function_performance1(suma_liczby, 500000, ))
# print(function_performance(suma_liczby2, 500000))
# print(function_performance(suma_liczby3, 500000))
# print(function_performance(suma_liczby4, 500000))
# print(function_performance(suma_liczby5, 500000))










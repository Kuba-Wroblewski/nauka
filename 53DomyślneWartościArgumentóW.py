#!/usr/bin/python3

"""
    Domyślne argumenty
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


def function_performance(func, arg, how_many_times=1):
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        koniec = time.perf_counter()
        sum = sum + (koniec - start)
    return sum


def function_performance1(func, arg, how_many_times=20):
    start = time.perf_counter()
    for i in range(0, how_many_times):
        func(arg)
        end = time.perf_counter()
    return end - start


print(suma_liczby(5000000))
print(function_performance1(suma_liczby, 500000, 20))
print(function_performance(suma_liczby, 500000, 20))
print(function_performance(suma_liczby2, 500000, 20))
print(function_performance(suma_liczby3, 500000, 20))
print(function_performance(suma_liczby4, 500000, 20))
print(function_performance(suma_liczby5, 500000, 20))

#!/usr/bin/python3

import time
# napisz funkcje która będzie sprawdzała czy jakis element znajduje sie w kontenerze.
# jesli sie znajduje funkcja ma zwrócic tak jak sie nie znajduje to ma wyswietlic nie i sprawdz co jest szybsze.


def function_performance(func, arg, how_many_times = 1):
    suma = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        suma += (end - start)
    return suma

setContainer = {i for i in range(1000)}
listaContainer = [i for i in range(1000)]

def find_element(liczba_szukana):
    if liczba_szukana in setContainer:
        return "Tak"
    else:
        return "Nie"

print(function_performance(find_element, 10, 50000))
# print(function_performance(find_element, 10, 500000))
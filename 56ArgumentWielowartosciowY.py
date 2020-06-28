#!/usr/bin/python3

import time

wybór = int(input("\nWpisz liczbą całkowitą\n"))

setContainer = {i for i in range(10, 100)}
listContainer = (i for i in range(10, 100))

def is_element_in(wybór, contener):
    if wybór in contener:
        return True
    else:
        return False

def performance_time(func, how_many_time=1, *arg):
    suma = 0

    for i in range(0, how_many_time):
        start = time.perf_counter()
        func(*arg)
        koniec = time.perf_counter()
        suma = suma + (koniec - start)
    return suma

print("suma_liczb", performance_time(is_element_in, 500000, wybór, setContainer))
print("suma_liczb2", performance_time(is_element_in, 500000, wybór, listContainer))

""" ARGUMENTY POZYCYJNE (NIENAZWANE) PRZED ARGUMENTAMI NAZWANYMI """

"""

def function_performance(func, *arg, how_many_times = 1)

*arg - deklaracja argumentu wielowartościowego, od tego momentu możemy przesłać więcej niż jeden argument nienazwany. Automatycznie po przesłaniu argumentu jest on krotką. Argumenty pozycyjne zawsze występują przed argumentami nazwanymi!

 print(function_performance(is_element_in, 1, setCointainer, how_many_times = 300))

def function_performance(func,how_many_times = 1, **arg);

** arg - argument wielowartościowy, nazwany który może przyjmować klucze - wartości. Ostatecznie argumenty po przesłaniu będą słownikiem.

 print(function_performance(is_element_in, 500, what_value = 500,
       container = setContainer,how_many_times = 300))

"""
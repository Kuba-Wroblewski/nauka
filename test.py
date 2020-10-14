#!/usr/bin/python3

<<<<<<< HEAD
print("warga sralga")

import time
# napisz funkcje która będzie sprawdzała czy jakis element znajduje sie w kontenerze.
# jesli sie znajduje funkcja ma zwrócić tak jak sie nie znajduje to ma wyswietlic nie i sprawdz co jest szybsze.

def function_performance(func, how_many_times=1, **arg):
    suma = 0
    print(arg.get("liczba_szukana"))
    # print(arg[0])
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        suma += end - start
=======
>>>>>>> update
    return suma


setContainer = {i for i in range(1000 + 1)}
listaContainer = [i for i in range(1000 + 1)]


print(function_performance(find_element, 1000, liczba_szukana=10, container=setContainer))
# print(function_performance(find_element, 1000, 10, setContainer))
# print(function_performance(find_element, 10, setContainer, how_many_times=1000))


#!/usr/bin/python3

import time
"""
napisz program ktory policzy sumę liczb od 1 do podanej liczby przez uzytkownika

dla np.5
1+2+3+4+5
zwroci
15
"""

def sumuj_do(liczba):
    wynik = 0
    for element in range(1, liczba + 1):
        wynik = wynik + element
    return wynik

def sumuj_do1(liczba):
    wynik = []
    for element in range(1, liczba + 1):
        wynik.append(element)
    return sum(wynik)

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba +1)])

def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1, liczba +1)})

def sumuj_do4(liczba):
    return sum((liczba for liczba in range(1, liczba +1)))

def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba

"""
wzór na ciąg arytmetyczny w matematyce
(1+liczba) / 2 * liczba
13 * 25
10* 25 = 250
3 * 25 = 75
250 + 75 = 325
"""

go = time.perf_counter()
print("Sumuj: ", sumuj_do(25665555))
end = time.perf_counter()
print("Sumuj czas: ", end - go)

go = time.perf_counter()
print("Sumuj1: ", sumuj_do1(25665555))
end = time.perf_counter()
print("Sumuj czas1: ", end - go)

go = time.perf_counter()
print("Sumuj2: ", sumuj_do2(25665555))
end = time.perf_counter()
print("Sumuj czas2: ", end - go)

go = time.perf_counter()
print("Sumuj3: ", sumuj_do3(25665555))
end = time.perf_counter()
print("Sumuj czas3: ", end - go)

go = time.perf_counter()
print("Sumuj4: ", sumuj_do4(25665555))
end = time.perf_counter()
print("Sumuj czas4: ", end - go)

go = time.perf_counter()
print("Sumuj5: ", sumuj_do5(25665555))
end = time.perf_counter()
print("Sumuj czas5: ", end - go)










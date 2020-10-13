#!/usr/bin/python3

"""
napisz program ktory policzy sumę liczb od 1 do podanej liczby przez uzytkownika

dla np.5
1+2+3+4+5
zwroci
15
"""

def sumuj_do():
    wynik = 0
    wybor = int(input("\nWprowadz liczbe do której bedziemy sumować liczby od 1\n"))
    for element in range(1, wybor + 1):
        wynik = wynik + element
    return wynik

def sumuj_do1():
    wynik = []
    wybor = int(input("\nWprowadz liczbe do której bedziemy sumować liczby od 1\n"))
    for element in range(1, wybor + 1):
        wynik.append(element)
    return sum(wynik)

def sumuj_do2():
    wybor = int(input("\nWprowadz liczbe do której bedziemy sumować liczby od 1\n"))
    return sum([liczba for liczba in range(1, wybor +1)])

def sumuj_do3():
    wybor = int(input("\nWprowadz liczbe do której bedziemy sumować liczby od 1\n"))
    return sum({liczba for liczba in range(1, wybor +1)})

def sumuj_do4():
    wybor = int(input("\nWprowadz liczbe do której bedziemy sumować liczby od 1\n"))
    return sum((liczba for liczba in range(1, wybor +1)))

def sumuj_do5():
    wybor = int(input("\nWprowadz liczbe do której bedziemy sumować liczby od 1\n"))
    return ((1 + wybor) / 2 * wybor)

"""
wzór na ciąg arytmetyczny w matematyce
(1+liczba) / 2 * liczba
13 * 25
10* 25 = 250
3 * 25 = 75
250 + 75 = 325
"""

# print(sumuj_do())
# print(sumuj_do1())
# print(sumuj_do2())
# print(sumuj_do3())
# print(sumuj_do4())
# print(sumuj_do5())
#!/usr/bin/python3

"""
napisz program ktory policzy sumę liczb od 1 do podanej liczby przez uzytkownika

dla np.5
1+2+3+4+5
zwroci
15
"""

wynik = []
wybor = int(input("\nWprowadz liczbe do której bedziemy sumować liczby od 1\n"))
for element in range(1, wybor + 1):
    wynik.append(element)
print(sum(wynik))




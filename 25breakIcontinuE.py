#!/usr/bin/python3

"""
break
continue
"""

wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj dodatnią liczbę:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia")
        continue
    print("Aktualny wynik dodawania to:", wynik)
    i += 1

"""
doda
3 parzyste kolejne liczby


1. break
2.coyinue
3.%
4
"""
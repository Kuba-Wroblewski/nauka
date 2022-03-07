#!/usr/bin/python3

"""
wynik = 0
i = 0
while i < 4:
    x = int(input("Podaj nam liczbę:\n"))
    wynik += x
    i += 1
print("Wynik dodawania liczb to:", wynik)

"""

for i in range(200):
    if (i % 5 == 0 and i % 7 == 1):
        print("Liczba", i, " jest podzielna przez 5 i nie jest podzielna przez 7")

# i % 5 == 0 Czyli: jeśli liczba jest podzielna przez 5 to wypadnie nam 0 jeśli nie jest
# to wypadnie nam 1 np. 5%5 = 0, 4%5 = 4

# przy 7 mamy 1%7 = 1, 2%7 = 2, 6%7 = 6, 7%7 = 0.

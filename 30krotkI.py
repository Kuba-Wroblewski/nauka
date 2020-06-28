#!/usr/bin/python3

"""
Krotka - to pojemnik do przechowywania wartości. Zawartości krotki
nie możemy później zmienić.

Krotkę możemy tworzyć na dwa sposoby :

  krotka = 1, 42, 12, -4         tj. bez nawiasów

    krotka = (1,42,12,-4)   przy pomocy okrągłych nawiasów


Z krotki korzystamy, gdy spodziewamy się wartości zmiennych,
które będą niezmienialne do końca działania programu.
Krotka pozwala na zaoszczędzenie miejsca w pamięci,
jak również przyspieszenie sprawności programu.

"""

krotka = (1, 23, 23, 4, -43)

print(krotka)
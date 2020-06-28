#!/usr/bin/python3

"""
    choice - zwraca losowy element
    choices - zwraca listę elementów i ma większe mozliwości

"""

import random

movieList = ["Tytuł 1", "Tytuł 2", "Tytuł 3", "Tytuł 4"]
event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata zdrowia"]
nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "purpurowa", "legendarna"]


from collections import Counter

print(random.choices(event))
nagroda100prob = random.choices(nagrodaZeSkrzynki, k = 50)
print(nagroda100prob.count("zielona"))

print(Counter(random.choices(nagrodaZeSkrzynki, [80, 15, 4, 1], k = 100)))

"""
    powyżej funkcja Counter tworzy słownik z wartością i kluczem. poprzez funkcje choices.
    możemy zwrócic liste elementów wraz z mozliwoscią ustawienia ile razy ma losować wybór i
    jakie mają być szanse wylosowania.
"""

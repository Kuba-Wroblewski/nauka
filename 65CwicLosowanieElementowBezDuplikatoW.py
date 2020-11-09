#!/usr/bin/python3

import random

"""
set nam gwarantuję że się powturzą elementy
"""

cardList = [ "9", "9", "9", "9",
             "10", "10", "10", "10",
             "Jack", "Jack", "Jack", "Jack",
             "King", "King", "King", "King",
             "Queen", "Queen", "Queen", "Queen"
             "Ace", "Ace", "Ace", "Ace",
             "Joker", "Joker"
       ]

random.shuffle(cardList)
print(random.sample(cardList, 5))
print(random.sample(set(cardList), 5), "\n")


lista_kart = []
karta = cardList.pop()
lista_kart.append(karta)
karta = cardList.pop()
lista_kart.append(karta)
karta = cardList.pop()
lista_kart.append(karta)
karta = cardList.pop()
lista_kart.append(karta)
karta = cardList.pop()
lista_kart.append(karta)
karta = cardList.pop()
lista_kart.append(karta)
karta = cardList.pop()
lista_kart.append(karta)
karta = cardList.pop()
lista_kart.append(karta)
print(lista_kart)


"""
Napisz funkcję, która zasymuluje jak działa lotto,
tzn. wybierze 6 unikalnych liczb z np. 49

sample - próbka/przykład gwarantuje nam unikalne wartości jeśli wewnątrz takie są.
"""

def choose_random_numbers(amount, total_amount):
    kontenerekLotto = []
    while len(kontenerekLotto) < 6:
        losa_liczba = random.randint(amount, total_amount)
        if losa_liczba in kontenerekLotto:
            continue
        else:
            kontenerekLotto.append(losa_liczba)
    print(kontenerekLotto)

choose_random_numbers(0, 49)


def choose_random_number(amount, total_amount):
    print(random.sample(range(total_amount + 1), amount))

choose_random_number(6, 49)
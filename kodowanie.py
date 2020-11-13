#!/usr/bin/python3

import random; from collections import Counter

movieList = ["Tytuł1", "Tytuł2", "Tytuł3", "Tytuł4"]
nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "purpurowa", "legendarna"]
# Czyli szansa na wystąpienie :
# Zielony - 80 %
# Pomarańcz - 15%
# Purpurowy - 4 %
# Legendarny - 1 %

# print(Counter(random.choices(nagrodaZeSkrzynki, [80, 15, 4, 1], k=100)))

cardList = [ "9", "9", "9", "9",
             "10", "10", "10", "10",
             "Jack", "Jack", "Jack", "Jack",
             "King", "King", "King", "King",
             "Queen", "Queen", "Queen", "Queen"
             "Ace", "Ace", "Ace", "Ace",
             "Joker", "Joker"
       ]


def choose_random_number(amount, total_amount):
    kontenerek = []
    while len(kontenerek) < 6:
        losa_liczba = random.randint(amount, total_amount)
        if losa_liczba in kontenerek:
            continue
        else:
            kontenerek.append(losa_liczba)
    print(kontenerek)

choose_random_number(0,5)









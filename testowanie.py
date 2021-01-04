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
print(random.sample(set(cardList),5))

"""
Napisz funkcję, która zasymuluje jak działa lotto,
tzn. wybierze 6 unikalnych liczb z np. 49

sample - próbka/przykład gwarantuje nam unikalne wartości jeśli wewnątrz takie są.
"""



# def choose_random_numbers(amount, total_amount):
#     box = []
#     while len(box) < 6:
#         losowa_liczba = random.randint(amount, total_amount)
#         if losowa_liczba in box:
#             continue
#         else:
#             box.append(losowa_liczba)
#     print(box)
# choose_random_numbers(0, 6)

# def choose_random_numbers(amount, total_amount):
#     print(random.sample(range(total_amount), 4))
# choose_random_numbers(0, 6)
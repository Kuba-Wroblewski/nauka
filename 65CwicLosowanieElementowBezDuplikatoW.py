#!/usr/bin/python3

import random

"""
set nam gwarantuję że się powturzą elementy


zrob liste która przechowa liste kart jednego i drugiego gracza 
i aby karty wylosowane dla graczy znikały z całej tali
"""

cardList = [ "9", "9", "9", "9",
             "10", "10", "10", "10",
             "Jack", "Jack", "Jack", "Jack",
             "King", "King", "King", "King",
             "Queen", "Queen", "Queen", "Queen",
             "Ace", "Ace", "Ace", "Ace",
             "Joker", "Joker"
       ]


print(len(cardList),'\n')
def random_list_gamer_1(total_amount):
    random.shuffle(cardList)
    karty_gracza_1 = []
    x = 0
    print(' Karty Gracza 1 :')
    while x < 4:
       x += 1
       karty_gracza_1 = total_amount.pop()
       print(karty_gracza_1)
random_list_gamer_1(cardList)

def random_list_gamer_2(total_amount):
    random.shuffle(cardList)
    karty_gracza_2 = []
    x = 0
    print('\n Karty Gracza 2 :')
    while x < 4:
       x += 1
       karty_gracza_2 = total_amount.pop()
       print(karty_gracza_2)
random_list_gamer_2(cardList)
print('\n',len(cardList))


"""
Napisz funkcję, która zasymuluje jak działa lotto,
tzn. wybierze 6 unikalnych liczb z np. 49

sample - próbka/przykład gwarantuje nam unikalne wartości jeśli wewnątrz takie są.
"""


def choose_random_numbers(amount, total_amount):
    box = []
    while len(box) < 6:
        losowa_liczba = random.randint(amount, total_amount)
        if losowa_liczba in box:
            continue
        else:
            box.append(losowa_liczba)
    print(box)
choose_random_numbers(0, 6)

def choose_random_numbers(amount, total_amount):
    print(random.sample(range(total_amount), 4))
choose_random_numbers(0, 6)

#!/usr/bin/python3

import random


cardList = ["9", "9", "9", "9",
             "10", "10", "10", "10",
             "Jack", "Jack", "Jack", "Jack",
             "King", "King", "King", "King",
             "Queen", "Queen", "Queen", "Queen",
             "Ace", "Ace", "Ace", "Ace",
             "Joker", "Joker"]


random.shuffle(cardList)

cardlist_gracz1 = []
cardlist_gracz2 = []
cardlist_gracz3 = []

def rozdawanie_kart():
    print(len(cardList))
    for x in range(0, 5):
        cardlist_gracz1.append(cardList.pop())
        cardlist_gracz2.append(cardList.pop())
        cardlist_gracz3.append(cardList.pop())

    print("Karty Gracza 1cardlist_gracz1", cardlist_gracz1)
    print("Karty Gracza 1cardlist_gracz2", cardlist_gracz2)
    print("Karty Gracza 1cardlist_gracz3", cardlist_gracz3)

rozdawanie_kart()
print(len(cardList))

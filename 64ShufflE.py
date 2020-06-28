#!/usr/bin/python3

"""
    ahuffle - randomizes entire list
    zmienia kolejność elementó wewnątrz.
    działą na orginale miesza kolejnośc
"""

import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "King", "King", "King", "King",
            "Queen", "Queen", "Queen", "Queen"
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]


random.shuffle(cardList)
print(cardList)
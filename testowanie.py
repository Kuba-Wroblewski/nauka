#!/usr/bin/python3

import random
from enum import Enum

Event = Enum("Event", ["Chest", "Nothing"])
EventProbability = {Event.Chest: 0.6, Event.Nothing: 0.4}
ListEvent = list(EventProbability.keys())
ListEventProbability = list(EventProbability.values())

Color = Enum("Color", {'Zielona':'Green', 'Pomarańczowa': 'Orange', 'Fioletowa': 'Purple', 'Złota': 'Gold'})
ColorProbability = {Color.Zielona: 0.75, Color.Pomarańczowa: 0.20, Color.Fioletowa: 0.04, Color.Złota: 0.01}
ListColor = list(ColorProbability.keys())
ListColorProbability = list(ColorProbability.values())

RewardFromChest = {  ListColor[reward]:
                    (reward + 1) * (reward + 1) * 1000
                    for reward in range(len(ListColor))}

def LowandHigh(amount, procent):
    low = amount - (procent / 100) * amount
    high = amount + (procent / 100) * amount
    return random.randint(low, high)

depth = 5
Gold = 0

while depth > 0:
    GamerAnser = input("Do You wont go forward ?\n")
    if GamerAnser == "y":
        print("Exelent, You go forward, Maybe You win something...")
        RewardChest = random.choices(ListEvent, ListEventProbability)[0]
        if RewardChest == Event.Chest:
            print("Congratulation !, You win a Chest")
            RewardColorChest = random.choices(ListColor, ListColorProbability)[0]
            RewardGame = LowandHigh(RewardFromChest[RewardColorChest], 10)
            print("Your Color Chest is:", RewardColorChest.value, "in this Chest is:", RewardGame, "Złota")
            Gold += RewardGame
        elif RewardChest == Event.Nothing:
            print("Unfortunatly You dont win anything.")
    else:
        print("You go only forward in this little game.")
        continue
    depth -= 1
if Gold > 0:
    print("Congratulation ! PIF PAF In Your 5 steps You Win:", Gold, "Złota")
else:
    print("Unfortunatly You dont win anything.")
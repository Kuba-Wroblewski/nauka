#!/usr/bin/python3

import random
from enum import Enum

Event = Enum("Event", ["Chest", "Nothing"])
EventProbability = {Event.Chest: 0.6, Event.Nothing: 0.4}
ListEvent = list(EventProbability.keys())
listEventProbability = list(EventProbability.values())

Color = Enum("Color", {"Zielony": "Green", "Pomarańczowy": "Orange", "Fioletowy": "Purple", "Złoty": "Gold"})
ColorProbability = {Color.Zielony: 0.75, Color.Pomarańczowy: 0.2, Color.Fioletowy: 0.04, Color.Złoty: 0.01}
listColor = list(ColorProbability.keys())
listColorProbability = list(ColorProbability.values())

ForChestReward = {listColor[reward]:
                      (reward + 1) * (reward + 1) * 1000
                  for reward in range(len(listColor))}


def LowandHigh(amount, procent):
    low = amount - (procent / 100) * amount
    high = amount + (procent / 100) * amount
    return random.randint(low, high)


depth = 5
Gold = 0

while depth > 0:
    GameAnser = input("Do You wont go forward ?\n")
    if GameAnser == "y":
        print("Exelent, You go forward, maybe You win something.")
        RewardChest = random.choices(ListEvent, listEventProbability)[0]
        if RewardChest == Event.Chest:
            ColorChest = random.choices(listColor, listColorProbability)[0]
            print("Congratulation, You win a Chest, color Your Chest is:", ColorChest.value)
            GameReward = LowandHigh(ForChestReward[ColorChest], 10)
            print("You open the Chest, and You see:", GameReward, "Złota")
            Gold += GameReward
        elif RewardChest == Event.Nothing:
            print("Unfortunatly, You dont win anything.")
    else:
        print("In this little game You go only forward, just tab <y>")
        continue
    depth -= 1
if Gold > 0:
    print("\nCongratulation !, In Your 5 step in this game You win:", Gold, "Złota")
else:
    print("\nUnfortunatly, You dont win anything.")

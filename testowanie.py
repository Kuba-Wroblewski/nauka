#!/usr/bin/python3

import random
from enum import Enum

Event = Enum('Event', ['Chest', 'Nothing'])
EventProbability = {Event.Chest: 0.6, Event.Nothing: 0.4}
EventList = list(EventProbability.keys())
EventListProbability = list(EventProbability.values())

Color = Enum('Color', {'Zielona': 'Green', 'Pomarańczowa': 'Orange', 'Fioletowa': 'Purple', 'Złota': 'Gold' })
ColorProbability = {Color.Zielona: 0.75, Color.Pomarańczowa: 0.20, Color.Fioletowa: 0.04, Color.Złota: 0.01}
ColorList = list(ColorProbability.keys())
ColorListProbability = list(ColorProbability.values())

RewardForChest = {  ColorList[reward]:
                    (reward + 1) * (reward + 1) * 1000
                    for reward in range(len(ColorList))}

def LowandHigh(amount, procent):
    low = amount - (procent / 100) * amount
    high = amount + (procent / 100) * amount
    return random.randint(low, high)

depth = 5
Gold = 0

while depth > 0:
    GamerAnser = input("Do You go wont forward ?\n")
    if GamerAnser == "y":
        print("Exelent You go forward, maybe You win something...")
        RewardChest = random.choices(EventList, EventListProbability)[0]
        if RewardChest == Event.Chest:
            print("Congratulation You win a chest !")
            RewardColorChest = random.choices(ColorList, ColorListProbability)[0]
            print("Yours chest color is:", RewardColorChest.value)
            GameReward = LowandHigh(RewardForChest[RewardColorChest], 10)
            print('Your reward from', RewardColorChest.value, 'chest is:', GameReward, 'złotych')
            Gold += GameReward
        elif RewardChest == Event.Nothing:
            print("In Your steps, You dont win.") 
    else:
        print("You can just go forwad in this game !. just tab <y>")
        continue
    depth -= 1
if Gold > 0:
    print("Congratulation Your reward Gold in 5 steps is:", Gold, "złotych")
else:
    print("Unfortunetly You win nothing")

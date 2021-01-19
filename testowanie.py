#!/usr/bin/python3

import random
from enum import Enum

Event = Enum(   'Event', ['cheast', 'nothing'])
eventDictionery = { Event.cheast: 0.6, Event.nothing: 0.4}

listEvenDictionery = list(eventDictionery.keys())
listEventProbability = list(eventDictionery.values())

Color = Enum( 'Color', {'zielona': 'Green', 'pomaranczowa': 'Orange', 'fioletowa': 'Purple', 'zlota': 'Gold'})
colorDictionery = {Color.zielona: 0.75, Color.pomaranczowa: 0.20, Color.fioletowa: 0.04, Color.zlota: 0.01}
  
listColor = list(colorDictionery.keys())
listColorProbability = list(colorDictionery.values())

rewardForCheast = { listColor[reward]:
                    (reward + 1) * (reward + 1) * 1
                    for reward in range(len(listColor))}

print("Welcome in my game KOMNATA, we will see how many Gold you win in 5 steps only forward.")
depth = 5
Gold = 0

while depth > 0:
    gamersAnser = input("Do you go to forward ?\n")
    if gamersAnser == "y":
        print("Exelent i wish you luckly, let's see what you win...")
        gamerWin = random.choices(listEvenDictionery, listEventProbability)[0]
        if gamerWin == Event.cheast:
            print("You win a cheast")
            cheastColor = random.choices(listColor, listColorProbability)[0]
            gamerReward = rewardForCheast[cheastColor]
            Gold += gamerReward
            print("The cheast color You win is:", cheastColor.value, "In this cheast is:", gamerReward, "sztab złota")
        elif gamerWin == Event.nothing:
            print("You don't win a cheast, unlucky")
    else:
        print("in this game you go only forwart, just smal game. Just tab <y>")
        continue
    depth -= 1

if Gold > 0:
    print("You win in Your 5 steps", Gold, "sztabek złota")
else:
    print("You are so unlucky, You nothing win. What a shejm")
    

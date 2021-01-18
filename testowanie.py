#!/usr/bin/python3

import random
from enum import Enum


Event = Enum(   'Event', ['cheast', 'nothing'])
eventDictionery = { Event.cheast: 0.6, Event.nothing: 0.4}

listEvenDictionery = list(eventDictionery.keys())
listEventProbability = list(eventDictionery.values())

Color = Enum( 'Color', {'zielona': 'green', 'pomaranczowa': 'Orange', 'fioletowa': 'purple', 'zlota': 'Gold'})
colorDictionery = {Color.zielona: 0.75, Color.pomaranczowa: 0.20, Color.fioletowa: 0.04, Color.zlota: 0.01}
  
listColor = list(colorDictionery.keys())
listColorProbability = list(colorDictionery.values())


print("Welcome in my game KOMNATA, we will see how many Gold you win in 5 steps only forward.")
depth = 5
Gold = 0

while depth > 0:
    gamersAnser = input("Do you go to forward ?\n")
    if gamersAnser == "y":
        print("Exelent i wish you like, let's see what you win...")
        gamerWin = random.choices(listEvenDictionery, listEventProbability)[0]
        if gamerWin == Event.cheast:
            print("You win a cheast")
            cheastColor = random.choices(listColor, listColorProbability)[0]
            
        elif gamerWin == Event.nothing:
            print("You don't win a cheast, unlucky")

        
    else:
        print("in this game you go only forwart, just smal game. Just tab <y>")
        continue

    
    depth -= 1
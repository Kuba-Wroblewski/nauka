#!/usr/bin/python3

import random
from enum import Enum

Event = Enum('Event',['Chest', 'Empty'])

eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                    }
eventList = list(eventDictionary.keys())
eventProbility = list(eventDictionary.values())


print("Welcome in my game name = BTC_UP")
print("""You have only 5 steps to be a rich guy :),
        Don't wory be happy""")


Colours = Enum('Colours', {'Green': 'zielony',
                        'Orange': 'pomarańczowy',
                        'Purple': 'fioletowy',
                        'Gold': 'złoty'
                        })

chestColoursDictionary = {  Colours.Green :  0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
                         }

chestColourList = tuple(chestColoursDictionary.keys())
chestColourProbability = tuple(chestColoursDictionary.values())

gameLength = 5

while gameLength > 0:
    gameAnser = input("Do you want to move forward?")
    if (gameAnser == "yes"):
        print("Great, let's see what you got...")
        randomEvent = random.choices(eventList, eventProbility)[0]
        if (randomEvent == Event.Chest):
            print("You have win a CHEST")
            randomChest = random.choices(chestColourList, chestColourProbability)[0]
            print("The chest color is:", randomChest)
        elif (randomEvent == Event.Empty):
            print("Tou have win nothing, you are so unlucky")

    else:
        print("You can go only forward")
        continue
    gameLength -= 1

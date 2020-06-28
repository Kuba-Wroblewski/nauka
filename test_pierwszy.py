#!/usr/bin/python3

import random
from collections import Counter


def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0, 100)
    if (isHitChance < weaponChanceToHitPercentage):
        return "Hit"
    else:
        return "Not hit"
print(will_weapon_hit(50))

x = 0
listHit = []
while x < 100:
    x += 1
    listHit.append(will_weapon_hit(50))

print(listHit)
print(listHit.count("Hit"))
print(listHit.count("Not hit"))

discionary = Counter(listHit)
print(discionary)

movieList = ["Tytuł 1", "Tytuł 2", "Tytuł 3", "Tytuł 4"]
event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata zdrowia"]
nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "purpurowa", "legendarna"]

print(Counter(random.choices(movieList, [10, 10, 10, 70], k=100)))



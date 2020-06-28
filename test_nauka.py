#!/usr/bin/python3

import random
from collections import Counter

def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0, 100)
    if (isHitChance < weaponChanceToHitPercentage):
        return "Hit"
    else:
        return "Not hit"


x = 0

listHit = []

while x < 100:
    x += 1
    listHit.append(will_weapon_hit(50))
print(listHit.count("Hit"))
print(listHit.count("Not hit"))
dictionaryHit = Counter(listHit)
print(dictionaryHit)

x = 0
while x < 100:
    x += 1
    print(random.randint(0, 10))
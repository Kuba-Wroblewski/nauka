#!/usr/bin/python3

import random



def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0,100)
    if (isHitChance < weaponChanceToHitPercentage):
        return "hit"
    else:
        return "not hit"

print(will_weapon_hit(50))

x = 0
listHit = []
while x < 100:
    x = x + 1
    listHit.append(will_weapon_hit(50))

print(listHit)
print(listHit.count("hit"))

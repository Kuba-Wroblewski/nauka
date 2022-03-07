#!/usr/bin/python3

"""
    random - (z ang. losowy) moduł po zaimportowaniu dostarcza nam kilka funkcji
random 0 <= x < 1 lub [0,1)
    uniform - w tej funkcji jako pierwszy argument przesyłamy początek losowania,
następnym argumentem jest koniec losowanie np. licząc od 2.5 bez uwzględnienia 10.
    uniform (2.5, 10.0) 2.5<= x <10.0 lub [2.5,10)
randrange - wylosuje liczby całkowite podane w zakresie puli oraz wybierze
 jedną z tych z wartości.
    randrange(10) z puli (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
randrange parzyste z puli  - podajemy liczby w zakresie
od ... do ... następnie wypisujemy “step” - wielokrotność liczby,
które mają być tworzone () przez co otrzymujemy i losujemy jedna z nich
    (0, 15, 2) parzyste z puli (0,2,4,6,8,10,12,14)
randint - przyjmuje pełną podaną wartość np. od 0 do 4 włącznie  np.
        randint(0,4) lub [0,4)
"""

import random


def will_weapon_hit(weaponChanceToHitPerception):
    isHitChance = random.uniform(0, 100)
    if (isHitChance < weaponChanceToHitPerception):
        return "hit"
    else:
        return "not hit"


x = 0
listHit = []
while x < 1000:
    x = x + 1
    listHit.append(will_weapon_hit(50))

print(listHit)
print(listHit.count("hit"))
print(listHit.count("not hit"))

from collections import Counter

dictionaryHit = Counter(listHit)
print(dictionaryHit)

x = 0

while x < 10:
    x = x + 1
    print(random.randint(0, 10))

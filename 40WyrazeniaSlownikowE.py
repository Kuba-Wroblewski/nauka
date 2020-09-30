#!/usr/bin/python3

"""
Wyrażenie słownikowe "{}" różni się od wyrażenia listowego tym ze
na początku podajey co ma się stać z kluczem i wartością

Wyrażenie słownikowe to formuła do tworzenia słowników na podstawie innych juz np. list.
"""

names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}
numbers = [1, 2, 3, 4, 5, 6]
celcius = {"t1": -20, "t2": -16, "t3": 0, "t4": 12, "t5": 24}

lennames = {
    name : len(name)
    for name in names
    if name.startswith("A")
}
print(lennames)

mnozenieliczb = {
    number: number ** 5
    for number in numbers
}
print(mnozenieliczb)

farenhait = {
    key : celcius *1.8 + 32
    for key, celcius in celcius.items()
    if celcius > -5
    if celcius < 20
}

print(farenhait)


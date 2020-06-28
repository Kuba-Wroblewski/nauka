#!/usr/bin/python3

"""
    Znajdz liczby od 100 do 470 włącznie, które są:
    podzielne przez 7, ale nie są podzielne przez 5

    Z czego skorzystasz ?
    1) generator
    2) wyrazenia listowego
    3) wyrazenia zbioru
    4) wyrażenia słownikowe

"""
# 1)
liczby = (
    element
    for element in range(100, 471)
    if element % 7 == 0
    if element % 5 != 0
)
for element in liczby:
    print(element)

# 2)
liczby = [
    element
    for element in range(100, 471)
    if element % 7 == 0
    if element % 5 != 0
]
print(liczby)

# 3)
liczby = {
    element
    for element in range(100, 471)
    if element % 7 == 0
    if element % 5 != 0
}
print(liczby)
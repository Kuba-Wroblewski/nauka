#!/usr/bin/python3

"""
    obiekt do zmienna, która ma wiecej możliwości,
    można wywołać na nim "funkcje"
    może mieć więcej niż 1 wartość

    obiekty immutable: bool, int, float, tuple, str

    immutable - niezmienne
    mutable - zmienny
    = ZMIENA miejsca wskazywania na nowy adres, na inny obiekt

"""

a = 4
print(a.bit_length())

listSample = [1, 4, 512, 24]
print(id(listSample))
listSample2 = listSample
print(id(listSample2))
listSample2.append(465)
print(listSample)
print(listSample2)
listSample2[0] = 7
print(listSample)

a = 4
print(id(a))
b = a
print(id(b))
b = 7
print(id(b))

k = 4
h = 4
print("Objekt k", id(k))
print("Objekt h", id(h))

c = 5
print("Objekt c", id(c))


def add(c, amount=1):
    print(id(c))
    c = c + amount
    print(id(c))


add(c)


def append_element_to_list(listka, element):
    print(id(listka))
    a = [2, 4, 20]
    listka = a
    listka.append(element)
    print(id(listka))


print(id(listSample))
append_element_to_list(listSample, 5)
print(listSample)

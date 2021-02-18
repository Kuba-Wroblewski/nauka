#!/usr/bin/python3


def add(c, amount = 1):
    # return c
    c = c + amount
    print(c)

c = 1
add(c)

print(c)


# Przesyłasz wartość 10 do funkcji "add"
def add(amount=50):
    global c
    c = c + 100 + amount
    print(c)

c = 10
print(c)

add(c)

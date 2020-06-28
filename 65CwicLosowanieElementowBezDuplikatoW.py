#!/usr/bin/python3

import random

x = 0
liczba = []
def choose_random_numbers(amount, total_amount):
    global x

    while x < 6:
        liczba.append(random.randint(0, total_amount))
        x += 1
        if x not in liczba:
            liczba.append(random.randint(0, total_amount))



    print(set(liczba))



choose_random_numbers(0, 6)
print(liczba)


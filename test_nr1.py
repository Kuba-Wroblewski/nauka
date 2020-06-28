#!/usr/bin/python3
"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.
Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.
Skrzynki mają różne kolory.
Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
pomaranczowy - 4000,
fioletowy - 9000,
zlota - 16000

1 1 0+1
4 2 1 +1
9 3 2+1
16 4 3 +1

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku

"""

import random

listBox = ["zielona", "pomaranczowa", "fioletowa", "złota (legendarna)"]
listCash = {"zielona":1000, "pomaranczowa":4000, "fioletowa":9000, "złota":16000}

x = 0
ttpiggybank = []
while x < 5:
    choice = float(input("""\nWhere are You going in the Chamber ?\n
1 - You go straight
2 - you go left
3 - you go right
4 - Exit the program\n"""))
    x += 1

    def win_or_not():
        if choice

    if choice == 1:
        print("tak")

    elif choice == 2:
        print("kdsadfl")
    elif choice == 3:
        print("qweewqqwe")
    elif choice == 4:
        print("Exit the program")
        break



























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
from collections import Counter
import random

winBox = ["You win a BOX", "You not win a BOX"]
listBox = ["zielona", "pomaranczowa", "fioletowa", "złota (legendarna)"]
listCash = {"zielona": 1000, "pomaranczowa": 4000, "fioletowa": 9000, "złota": 16000}

x = 0
piggybank = []
while x < 5:
    choice = float(input("""\nWhere are You going in the Chamber ?\n
1 - You go straight
2 - you go left
3 - you go right
4 - Exit the program\n"""))
    x += 1
    if choice > 4:
        print("Error argument choice - please check your choice")
        continue


    def win_or_not_win_box():
        chancetowin = random.choices(winBox, [60, 40])
        return chancetowin


    if choice == 1 or 2 or 3:
        win = (win_or_not_win_box())
        if choice == 1:
            print("You go straight")
        elif choice == 2:
            print("You go left")
        elif choice == 3:
            print("You go right")
        elif choice == 4:
            print("Exit the program")
            break
        if win == ['You win a BOX']:
            piggybank.append(random.choices(listBox, [75, 20, 4, 1], k=1))
            print("You win a Box !")
        else:
            print("You win nothing :(")

howMuchBoxGreen = piggybank.count(['zielona']) * 1000
howMuchBoxOrange = piggybank.count(['pomaranczowa']) * 4000
howMuchBoxViolet = piggybank.count(['fioletowa']) * 9000
howMuchBoxGold = piggybank.count(['złota (legendarna)']) * 16000
winCash = [howMuchBoxGreen + howMuchBoxOrange + howMuchBoxViolet + howMuchBoxGold]

if piggybank != bool:
    print("\nYou Win a Box:")
    print(piggybank)
    print("You open the Box and You have got a gold:")
    print(winCash)
else:
    print("You win nothing")

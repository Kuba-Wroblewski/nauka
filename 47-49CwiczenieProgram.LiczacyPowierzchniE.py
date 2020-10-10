#!/usr/bin/python3

import figury
# Enumeration - spis - wyliczenie
from enum import IntEnum
Menu_Figury = IntEnum("Menu_Figury", "Kwadrat Prostokąt Koło Trójkąt Trapez Koniec")

while True:
    odpowiedz = float(input("""\nCo chcesz zrobic...?\n
1 - Oblicz pole kwadratu
2 - Oblicz pole prostokątu
3 - Oblicz pole koła
4 - Oblicz pole trójkąta
5 - Oblicz pole Trapezu
6 - Koniec programu\n"""))

    if odpowiedz == Menu_Figury.Kwadrat:
        a = float(input("Prosze podać długość jednego z boków kwadratu\n"))
        print("Pole kwadratu wynosi", figury.pole_kwadratu(a))

    elif odpowiedz == Menu_Figury.Prostokąt:
        a = float(input("Prosze podać długość jednego z boków prostokąta\n"))
        b = float(input("Prosze podać długość drugiego z boków prostokąta\n"))
        print("Pole prostokątu wynosi", figury.pole_prostokata(a, b))

    elif odpowiedz == Menu_Figury.Koło:
        r = float(input("Prosze podać promień koła\n"))
        print("Pole koła wynośi", figury.pole_kola(r))

    elif odpowiedz == Menu_Figury.Trójkąt:
        a = float(input("Prosze podać bok trójkąta\n"))
        h = float(input("Prosze podać wysokość trójkąta\n"))
        print("Pole trójkąta wynosi", figury.pole_trojkata(a, h))

    elif odpowiedz == Menu_Figury.Trapez:
        a = float(input("Prosze podać długość jednego z boków trapezu\n"))
        b = float(input("Prosze podać długość drugiego z boków trapeza\n"))
        h = float(input("Prosze podać wysokość trapezu\n"))
        print("Pole trapezu wynosi", figury.pole_trapezu(a, b, h))

    elif odpowiedz == Menu_Figury.Koniec:
        print("KONIEC PROGRAMU")
        break

    else:
        print("Podałeś błędny parametr z zakresu")

# from enum import IntEnum
# Menu_Dni_Tygodnia = IntEnum("Menu_Dni_Tygodnia", {"Poniedziałek":20, "Inny_dzien":1})
# print(list(Menu_Dni_Tygodnia))
# wybor = int(input("""\nJaki dziś dzień ?:
#     1. Poniedziałek
#     2. Inny dzień\n"""))
# if wybor == Menu_Dni_Tygodnia.Poniedziałek:
#     print("Może i poniedziałek")
# if wybor == Menu_Dni_Tygodnia.Inny_dzien:
#     print("Inny dzień")

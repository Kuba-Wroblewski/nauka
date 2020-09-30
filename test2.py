#!/usr/bin/python3

import figury
from enum import IntEnum
Menu_Figury = IntEnum('Menu_Figury', 'Kwadrat Prostokąt Trójkąt Trapez Koło Exit')

while(True):
    wybor = int(input("""\nWybierz figurę, której pole chcesz obliczyć:
    1. Kwadrat
    2. Prostokąt
    3. Trójkąt
    4. Trapez
    5. Koło
    6. Exit\n"""))

    if wybor == Menu_Figury.Kwadrat:
        a = int(input("Proszę wprowadzić bok kwadratu...\n"))
        print("Wynik pola powierzchni kwadratu:", figury.pole_kwadratu(a))
    if wybor == Menu_Figury.Prostokąt:
        a = int(input("Proszę wprowadzić pierwszy z boków prostokąta...\n"))
        b = int(input("Proszę wprowadzić drugi z boków prostokąta...\n"))
        print("Wynik pola powierzchni prostokąta:", figury.pole_prostokata(a, b))
    if wybor == Menu_Figury.Trójkąt:
        a = int(input("Proszę wprowadzić pierwszy z boków trójkąta...\n"))
        h = int(input("Proszę wprowadzić wysokość trójkąta - h...\n"))
        print("Wynik pola powierzchni trójkąta:", figury.pole_trojkata(a, h))
    if wybor == Menu_Figury.Trapez:
        a = int(input("Proszę wprowadzić pierwszy z boków trapezu...\n"))
        b = int(input("Proszę wprowadzić drugi z boków trapezu...\n"))
        h = int(input("Proszę wprowadzić wysokość trapeza -h...\n"))
        print("Wynik pola powierzchni trapezu:", figury.pole_trapezu(a, b, h))
    if wybor == Menu_Figury.Koło:
        r = int(input("Proszę wprowadzić promień koła -r...\n"))
        print("Wynik pole powierzchni koła:", figury.pole_kola(r))
    if wybor == Menu_Figury.Exit:
        print("Exit.")
        break


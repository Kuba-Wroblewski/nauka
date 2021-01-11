#!/usr/bin/python3
from enum import IntEnum
import figury

Menu_Figury = IntEnum('Menu_Figury', 'Kwadrat Prostokąt Koło Trójkąt Trapez')

print('Witamy w programie do liczenia obwodu figur')

wybór = int(input("""Podaj nazwę figury której obwód chcesz wyliczyć ?
            1. Kwadratu
            2. Prostokąta
            3. Koła
            4. Trójkąta
            5. Trapezu """ '\n' ))
            
if wybór == Menu_Figury.Kwadrat:
   print(Menu_Figury.Kwadrat)
   a = float(input("Wybrałeś Kwadrat, podaj długość jednego z boków\n"))
   print("Pole Kwadratu wynośi:", figury.pole_kwadratu(a))
elif wybór == Menu_Figury.Prostokąt:
   a = float(input("Wybrałeś Prostokąt, podaj długość jednego z boków\n"))
   b = float(input("Podaj długość drugiego bok Prostokąta\n"))
   print("Pole Prostokąta wynośi wynośi:", figury.pole_prostokata(a, b))
elif wybór == Menu_Figury.Koło:
   r = float(input("Wybrałeś Koło, podaj średnice okręgu\n"))
   print("Pole Koła wynośi:", figury.pole_kola(r))
elif wybór == Menu_Figury.Trójkąt:
   a = float(input("Wybrałeś Trójkąt, podaj długość jednego z boków Trójkąta\n"))
   h = float(input("Podaj wysokość Trójkąta tak zwaną wartość 'h'\n"))
   print("Pole Trójkąta wynośi:", figury.pole_trojkata(a, h))
elif wybór == Menu_Figury.Trapez:
   a = float(input("Wybrałeś Trapez, podaj długość jednego z boków\n"))
   b = float(input("Podaj długość drugiego boku Trapeza\n"))
   h = float(input("Podaj wysokość Trapeza tak zwaną wartość 'h'\n"))
   print("Pole Trapezu wynośi:", figury.pole_trapezu(a, b, h))
else:
   print("Podałeś parametrz z poza zakresu")
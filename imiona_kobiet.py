#!/usr/bin/python3

lista = ['Kasia', 'Basia', 'Asia', 'Justyna', 'Aldona', 'Beata', 'Monika']

x = input()
if (x) == 'Asia' in lista:
    print('znaleziono Asie')
elif (x) == 'Kasia' in lista:
    print('Nie znaleziono Asi, ale mamy cycki Kasi')
elif (x) == 'Beata' in lista:
    print('Nie mamy Asi, Ani cycków Kasi ale mamy za to Beate')
else:
    print('Nic nie znaleziono')

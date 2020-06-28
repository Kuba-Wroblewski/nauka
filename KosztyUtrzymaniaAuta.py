#!/usr/bin/python3

ocAc = 1300
oc = 800
przeglad = 160
paliwo = 250 * 12    # na miesiąc wiec * 12
amortyzacja = 170 + 30 + 40 + 30 + 40 + 150 * 2
naprawy = 5000  # jesli auto premium i jest starsze niz 10 lat koszt na rok
garaz = 101 * 12
oplataZaGrunt = 56 * 4 # 56 zł na kwartał
serwis = 1500 * 2   # co 15 tysiecy

print("Koszty utrzymania Superba na rok bez paliwa =", oc + przeglad + amortyzacja + naprawy + garaz + oplataZaGrunt)
print("Koszty utrzymania nowego auta na rok bez paliwa =", ocAc + przeglad + serwis + garaz + oplataZaGrunt)
print("Koszty utrzymania Superba co miesiac bez paliwa  =", (oc + przeglad + amortyzacja + naprawy + garaz + oplataZaGrunt) / 12)
print("Koszty utrzymania nowego auta co miesiąc =", (ocAc + przeglad + serwis + garaz + oplataZaGrunt) / 12)
print("Koszt średni paliwa na rok =", paliwo)
print("Koszt średni paliwa co miesiąc =", paliwo / 12)
print("Koszt garażu wraz z gruntem na rok/miesiąc =", garaz + oplataZaGrunt,"/", (garaz + oplataZaGrunt) / 12)
print("Koszt utrzymanai superba bez paliwa i bez garazu z gruntem na rok/miesiac =", oc + przeglad + amortyzacja + naprawy, "/", (oc + przeglad + amortyzacja + naprawy) /12)
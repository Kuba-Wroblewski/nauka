#!/usr/bin/python3


from enum import IntEnum
Menu_Dni_Tygodnia = IntEnum("Menu_Dni_Tygodnia", {"Poniedziałek":20, "Inny_dzien":25})
wybor = int(input("""\nJaki dziś dzień ?:
    1. Poniedziałek
    2. Inny dzień\n"""))
if wybor == Menu_Dni_Tygodnia.Poniedziałek:
    print("Może i poniedziałek")
if wybor == Menu_Dni_Tygodnia.Inny_dzien:
    print("Inny dzień")


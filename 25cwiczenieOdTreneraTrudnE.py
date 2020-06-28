#!/usr/bin/python3



wynik = 0
i = 0
while i < 3:
    x = int(input("Prosze podać liczbe dodatnią i parzystą: "))
    if (x > 0 and x % 2 == 0):
        wynik += x
    else:
        print("Liczba miała być dodatnia i parzysta")
        continue
    i += 1
print("Wynik sumy 3 kolejnych dodatnich parzystych cyfr to: ", wynik)


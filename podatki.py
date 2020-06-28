#!/usr/bin/python3

import time
time.sleep(1)
print('START')
print('')
time.sleep(1)
print('Wpisz swoje wynagrodzenie za ubiegły rok.')
print('Sprawdzimy jaki podatek zostanie ci nałożony')

liczba = int(input('Wpisz wartość brutto...'))


if liczba >= 30000 and liczba < 78000:
    x = 0.19
    time.sleep(1)
    print('Twój podatek to 19%')
if liczba > 78000 and liczba < 564000:
    x = 0.23
    time.sleep(1)
    print('Twój podatek to 23%. Jest to belka pod małe i średnie przedsiębiurstwa')
    print('Proponuje Ci umuwić się z naszym prawnikiem')
elif liczba >= 564000:
    x = 0.37
    time.sleep(1)
    print('Twój podatek to 37%. Przekroczył belke w średnich i dużych przdsiebiórstwach')
    print('Gratulacje !')
elif liczba < 30000:
    time.sleep(1)
    print('Twój podatek wynosi 0')
    x = 0
if x == 0:
    print('Twój podatek jest równy 0. Więc nie odejmujesz nic od dochodu. Brawo !')
else:
    print('')
    a = liczba * x
    time.sleep(1)
    print('Twój podatek z poprzedniego roku jaki musisz zapłącić to...')
    b = 'zł'
    print(a, b)

time.sleep(2)
print('')
print('KONIEC')
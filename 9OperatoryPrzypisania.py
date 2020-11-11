#!/usr/bin/python3

# OPERATORY PRZYPISANIA

'''
W taki sam sposób możesz korzystać z innych operatorów

+=    x += 5    to skrócony zapis: x = x + 5
-=    x -= 5    to skrócony zapis: x = x - 5
*=    x *= 5    to skrócony zapis: x = x * 5
/=    x /= 5    to skrócony zapis: x = x / 5
%=    x %= 5    to skrócony zapis: x = x % 5    # moduło (reszta z dzielenia)
//=    x //= 5    to skrócony zapis: x = x // 5 # dzielenie w dół
**=    x **= 5    to skrócony zapis: x = x ** 5 # potęgowanie
'''

x = 4   # x = x + wartość którą chcesz dodać do x np.
x = x + 3

'''
Interpreter czyta to co dzieje się pierw po prawej stronie, czyli szuka co znajduje się
pod zmienną x, następnie dodaje 4 + 3 i otrzymujesz wynik x równa się 7

Dużo szybszym i czytelniejszym zapisem jest
'''

x += 3     # dodaj do x (4 wyżej) liczbę 3. Wynik jest ten sam x równa się 7

x = 4
x *= 2         # x*2, Wynik to 4 * 2 = 8

a = b = c = d = e = f = g = 50
a += 5; b -= 5; c *= 5; d /= 5; e %= 5; f //= 5; g **= 5

print(a, b, c, d, e, f, g)
x = 53.5
print(x)
x %= 2.0
print(x)

x = 5
x //= 6
print(x)

x = 2
x **= 8
print(x)

x = 1
x **= 8
print(x)

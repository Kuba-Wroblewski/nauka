#!/usr/bin/python3

a = {1, 3, 50, -23, 42, 11, 11}
print(a)
a.add(11)   # nie doda po raz kolejny 11 ponieważ nie pozwała na dodawanie tych samych elementów unikalność musi zostać
a.add(2)    # doda liczbe 2 i ustawi jej automatyczna kolejność
print(a)


x = {1, 4, 5, 6, 8, 8, 8, 8, 20}
b = {1, 6, 5, 10, 3, 20}
print(x & b)    # zbiory mają ciekawa funkcje "&" wspólne elementy
print(x | b)    # wszystkie elementy w x i b w tym samym momencie bez powtórzeń unikalne
print( x ^ b)   # Alternatywa wykluczająca - wyklucza wspulne wartości po sumie. = (x | b) - ( x & b)
print(x - b)    # odejmmowanie zbiorów wynikiem jest odjęcie od zbioru x powtarzających sie elementów ze zbioru b

print(x.discard(8)) # usuwa element ze zbioru, jeśli nie ma tego elementu usuwanego to nie wyskoczy błąd
# print(x.remove(21)) - Wyskoczy błąd ponieważ tego elementu nie ma do usunięcia w zbiorze
print(set(x))
print(x.issubset(b))    # sprawdza czy 1-en zbiór jest podzbiorem 2-go

"""
Jak byśmy mieli
B = {1, 4}
A = {1, 4, 30, -4}
To w tym wypadku zbiór B jest podzbiorem zbioru A
"""
X = (1, 4, 5, 6, 8, 8, 8, 8, 20)
print(set(X))   # To w szybki sposób zmienia LISTĘ w ZBIÓR i ma unikalne elementy czyli usuwa duplikaty.
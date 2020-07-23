#!/usr/bin/python3

# len() - długość
# .append - dodać
# .extend - rozszerzać
# .insert(index, co) - wstawić
# .index - indeks danego el. pierwszego
# sort(reverse=False) - sortuj rosnąco
# max()
# min()
# .count - ile razy coś wystąpi
# .pop - usuń ostatni el.
# .remove - usuń pierwsze wystąpienie
# .clear - wyczyść liste
# .reverse - zmień kolejność

imiona = ["kuba", "wiola", "arek", "zenon"]
#            0       1        2       3
# w 4 elementowej liscie numeracja konczy sie na 3

liczby = [1, 43, -3, 50]
mieszana = [1, "asd", 42, "kuba"]

for imie in imiona:
    print(imiona[-2])


imiona[-1] = "wojtek"
print(imiona[-1])
print(imiona)

if 2 in liczby:
    print("liczba 2 znajduje sie w liscie")
else:
    print("Liczba 2 nie znajduje sie w liscie")

print(2 * liczby)
print(2 * imiona)
print([3] + imiona)


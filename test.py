#!/usr/bin/python3


imiona = ['kuba', 'wiola', 'arek', 'zenon']
#            0       1        2       3
# w 4 elementowej liscie numeracja konczy sie na 3

liczby = [1, 43, -3, 50]
mieszana = [1, "asd", 42, "kuba"]

print("kuba" in imiona)

if ("zenon" in imiona):
    print("cześć Zenku")

if 2 in liczby:
    print("liczba 2 znajduje sie w liscie")
else:
    print("Liczba 2 nie znajduje sie w liscie")

print(2 * liczby)
print(2 * imiona)
print([3] + imiona)


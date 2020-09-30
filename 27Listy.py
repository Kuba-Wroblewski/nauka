#!/usr/bin/python3

"""
Poniżej mamy najczęściej używane funkcje na listach
"""

# len() - długość                           - mozemy dzieki niej dowiedziec sie ile elementow ma lista
# .append - dodać                           - pozwala nam dodać elementy(liste) do końca listy
# .extend - rozszerzać                      - rozszerza nam liste o nowe elementy nadpisuje liste
# .insert(index, co) - wstawić              - możemy dodwać nowy element do listy podajać miejsce DODANIA
# .index - indeks danego el. pierwszego     - pozwoli nam odszukać index danego elementu
# sort(reverse=False) - sortuj rosnąco      - sortuje nam liste od najmniejszych do rosnących (domyślne)
# max()                                     - pokazuje nam maksymalna wartosc
# min()                                     - pokazuje nam minimalna wartosc
# .count - ile razy coś wystąpi             - liczy ile razy wystepuje element
# .pop - usuń ostatni el.                   - usuwa nam ostatni element pop-(trzaskać)
# .remove - usuń pierwsze wystąpienie       - usuwa nam dany element
# .clear - wyczyść liste                    - czyści nam liste całą
# .reverse - zmień kolejność                - odwraca kolejość

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

# len  dowiemy sie dzieki tej funkci ile ma elementów lista
print(len(liczby)); print(len(mieszana))
# append  dodaje do listy liste na stałe i jest szybszy od plusa "+"
liczby.append([9,54,3])
print(liczby)
#  extend rozszerza nam liste o nowe elementy, jest szybsze od dodawania "+"
liczby.extend([2,3,1,53])
print(liczby)
# insert  dodaje nam nowe elementy przesuwająć reszte za siebie, podajemy ich miejsce w liscie
imiona.insert(2, "kuba")
print(imiona)
#  index  pokaże nam idex szukanego elementu, index zwraca nam pierwsze wystąpienie
print(mieszana.index("asd"))
# sort  sortuje nam liste domyślnie, trzeba uważac aby lista nie była w liscie
liczby = [1, 43, -3, 50]
imiona.sort(); liczby.sort(); print(imiona); print(liczby), liczby.sort(reverse=True); print(liczby)
# max and min pokazuje nam max wartosc z listy a minimum pokazuje nam minimalną wartość z lista mieszana jest problem
print(max(liczby)); print(min(liczby)); print(max(imiona))
#  count  liczy nam ile razy występuje dany element
print(liczby.count(50))
# pop  usuwa ostatni element
mieszana.pop(); mieszana.pop(); print(mieszana)
# remove  usuwa nam jeden wybrany element
liczby.remove(-3)
print(liczby)
# clear  służy nam do czyszczenia listy
liczby.clear()
print(liczby)
# reverse  odwraca kolejność elementów
mieszana.reverse()
print(mieszana)

mieszana = [1, "asd"]
print(2 * mieszana)
print([3] + mieszana)
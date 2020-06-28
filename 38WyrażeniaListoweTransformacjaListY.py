#!/usr/bin/python3

liczby = [1, 2, 3, 4, 5, 6]

# Moja próba aby z listy zrobic drugą liste poprzez potegowanie każdej liczby z listy
liczby2 = []
for liczba in liczby:
    x = (liczba**2)
    liczby2.append(x)
if (len(liczby)) == (len(liczby2)):
    print(liczby2, "\n")

#  Przykład wykładowcy jak on to rozwiązał troche lepiej :)
potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)
    print(potegiDwojki)

#  Przykład przez trenera na liczbach parzystych
liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)
        print(liczbyParzyste)

# Przykłąd ponizej robi dokładnie to samo co przykłady powyżej
potegiDwojki2 = [element**2
                 for element in liczby
                 ]
print("\n",potegiDwojki2)

#  Przykłąd jak powyżej z liczbą parzysta ale krótszy.
LiczbyParzyste = [element
                  for element in liczby
                  if (element % 2 == 0)
                  ]
print(LiczbyParzyste)
# wyrazenie listowne jest to formuła które zastępuje w elegantszy sposób jakąs pętle która działą na listach w taki sposób jak tutaj.
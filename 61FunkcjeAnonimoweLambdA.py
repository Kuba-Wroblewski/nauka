#!/usr/bin/python3
def funkcjaLambda(x):
    if x % 2 == 0:
        return x

myList = [2, 14, 22, 7, 6, 4, 5, 17]

myListFiltered = list(filter(funkcjaLambda, myList))
myListFiltered2 = [x for x in myList if (x % 2) == 0]
myListFiltered3 = list(filter(lambda x: (x % 2) == 0, myList))

print(myListFiltered)
print(myListFiltered2)
print(myListFiltered3)


"""
Funkcje anonimowe - funkcje bez nazwy, mogą przyjmować argumenty.
 Używane są najczęściej do jednorazowych i szybkich operacji na kodzie.
  Aby stworzyć taką funkcję należy skorzystać ze słówka lambda. 


Stworzyliśmy listę liczb parzystych i nieparzystych.Chcemy
 przefiltrować liczby i wybrać te, które są parzyste. 

         my_list = [2, 14, 22, 7, 6, 4, 5, 17] 


Najlepiej skorzystać z funkcji o nazwie filtr (z ang. filter) - w której 
jako pierwszy argument podajemy funkcję, określamy jakie argumenty będzie
 przyjmować nasza funkcja, piszemy warunek jaki ma spełniać funkcja oraz 
 skąd ma pobrać dane 


filter(lambda x: x %2 == 0 , my_list)


Filtr zwraca nam obiekt filtrujący, który możemy zmienić ostatecznie w listę.

"""
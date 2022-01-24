#!/usr/bin/python3

# pętla


"""
Pętla  (z ang. while to “podczas”, “gdy”)  służy do zapętlania, czyli powtarzania danych instrukcji wielokrotnie. Pętla będzie się wykonywać, dopóki warunek będzie prawdziwy np.

liczba = 0
while liczba < 5:
         print(liczba)

ponieważ liczba się nie zmienia i cały czas jest równa 0 to ta pętla jest tzw. pętlą nieskończoną. Dzieje się tak ponieważ warunek będzie zawsze prawdziwy, 0 zawsze będzie mniejsze od 5.

Aby przerwać pętle nieskończoną naciskamy Ctrl + C ( przerwanie pętli)


Aby upewnić się, że pętla się zakończy należy zmienić zmienić warunek pętli w taki sposób, aby warunek kiedyś stał się fałszywy. Zmianę dokonujemy wewnątrz pętli np.

liczba = 0
while liczba < 5:
         print(liczba)
         liczba += 1
"""

liczba = 100
while liczba >= 0:
    print(liczba)
    liczba -= 1

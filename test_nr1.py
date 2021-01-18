#!/usr/bin/python3
import sys

# liczby = [1, 2, 3, 4, 5, 6]

liczby = [  liczba ** 2
            for liczba in range(101)
         ]
# print(sum(liczby))

liczbyGen = (  liczba ** 2
            for liczba in range(101)
         )

# print(sum(liczbyGen))

for item in liczbyGen:
   if item == 36:
      continue
      print("go go go go go")
   elif item == 81:
      break
   print(item)

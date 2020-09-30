#!/usr/bin/python3

# dictionary - słownik KLUCZ - WARTOŚĆ

pokoje = {49: "Arkadiusz Aloizy", 69: "Ada Sałatowska"}
print(pokoje)
pokoje[69] = "Iga Kowalska"
print(pokoje[69])
print(pokoje)

pokoje.update({40: "Jan Kowalski"})
print(pokoje)
del(pokoje[40])
print(pokoje)
print(len(pokoje))

lista = { "kupic": "makaron", 2: "auto"}

print(lista["kupic"])
lista.update({"kupi": "makaron"})
del(lista[2])
lista.update({2: "Auto"})

print(lista)
lista.pop("kupi")
print(lista)
lista.clear()
print(lista)

"""
dictionary - z ang. słownik 

Słownik to pojemnik do przechowywania danych. Każdy element słownika składa się z
 klucza i przypisanej mu wartości. Do klucza przypisywana jest jedna wartość. 
 Klucze muszą być unikalne (nie mogą się powtórzyć ich nazwy), natomiast wartość może się powtarzać.

Przykładowy słownik 

pokoje = {49: 'Arkadiusz Włodarczyk' , 69: 'Wioletta Włodarczyk'}

pokoje - nazwa słownika
{  } - klamry do utworzenia słownika
49, 69 - klucz
'Arkadiusz Włodarczyk' - wartość 


Aby pobrać wartość wpisujemy nazwę słownika, a po niej nazwę klucza w kwadratowych nawiasach np. 

        pokoje[49]   lub za pomocą funkcji get    pokoje.get(49)

Aby dodać wartość tworzymy nowy klucz i przypisujemy mu wartość lub za pomocą 
funkcji update (z ang.aktualizuj) np.

                pokoje.update({499:'Jasiu Kokoszka'})

Aby usunąć wartość ze słownika 

 za pomocą  del (z ang. usunąć)
 
              del(pokoje[499])    

za pomocą funkcji pop, która usuwa, ale zarazem zwraca wartość, która została usunięta

  pokoje.pop(400)

      -     funkcja popitem usuwa ostatni element i również go zwraca do użytku 
                    
             pokoje.popitem()
Aby sprawdzić ilość elementów w słowniku używamy :

      len(pokoje)

Aby wyczyścić słownik z elementów

            pokoje.clear()
"""
#!/usr/bin/python3

imiona = []
with open("imionatest.txt", "r") as file:
    for element in file:
        imiona.append(tuple(element.split()))
    print(imiona)

with open("imiona.txt", "w+") as file:
    for element in imiona:
        file.write(element[0] + "\n")

with open("nazwiska.txt", "w+") as file:
    for element in imiona:
        try:
            file.write(element[1] + "\n")
        except IndexError:
            file.write("\n")


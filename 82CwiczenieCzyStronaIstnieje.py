#!/usr/bin/python3

import requests

listaUrl = [ 'https://flask.palletsprojects.com/en/1.1.x/quickstart/', 'https://github.com/fuck', 'https://www.google.pl/', 'https://www.google.pl/nocos' ]



def work_url(listaUrl):
    list_work_url = []
    for element in listaUrl:
        response = requests.get(element)
        if response.status_code == 200:
            list_work_url.append(element + "\n")
                
        else:
            print("This page is not avaliable:", element, response)

print(list_work_url)


def work_url2(list_work_url):
    with open("work_url.txt", "w") as file:
        file.writelines(list_work_url)


work_url(listaUrl)

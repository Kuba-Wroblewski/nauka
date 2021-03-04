#!/usr/bin/python3

import requests # import Module

sample_file_url = [
                    'https://flask.palletsprojects.com/en/1.1.x/quickstart/', 'https://github.com/fuck',
                    'https://www.google.pl/', 'https://www.google.pl/nocos'
                   ]

my_work_url = []  # Variable 
def check_url(sample):  # Function
    for url in sample:
        response = requests.get(url)  # Module
        if response.status_code == 200:  # Function
            my_work_url.append(url)  # Variable
            # my_work_url.append(url + '\n') or this to add another url in new line
        else:
            print("This page is not available:", url, response)

def save_good_url(my_work_url):  # Function
    with open("work_url.txt", "w") as file:
        file.writelines(my_work_url)
# Save working url in new file

check_url(sample_file_url)
save_good_url(my_work_url)

'''
for url in lista_url:
    check_url(url)
with open("work_url.txt", "w") as file:
    file.writelines(my_work_url)
'''
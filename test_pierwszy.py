#!/usr/bin/python3

import requests

sample_file_url = [
                    'https://flask.palletsprojects.com/en/1.1.x/quickstart/', 'https://github.com/fuck',
                    'https://www.google.pl/', 'https://www.google.pl/nocos'
                   ]  # Sample url to test

my_work_url = [] 
def check_url(sample):
    for url in sample:
        response = requests.get(url)  # Check response sample url 
        if response.status_code == 200: 
            my_work_url.append(url)
        else:
            print("This page is not available:", url, response)

def save_good_url(my_work_url):
    with open("work_url.txt", "w") as file:
        file.writelines(my_work_url)

check_url(sample_file_url)
save_good_url(my_work_url)

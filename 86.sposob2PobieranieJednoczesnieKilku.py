#!/usr/bin/python3

import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/todos')

def count_task_frequency(tasks):
    completedTasksFrequencyByUsers = dict()
    for entry in tasks:
        if entry['completed'] == True:
            try:
                completedTasksFrequencyByUsers[entry['userId']] += 1
            except KeyError:
                completedTasksFrequencyByUsers[entry['userId']] = 1
    
    return completedTasksFrequencyByUsers

def get_users_with_top_tasks(completedTasksFrequencyByUsers):
    useridWithMaxAmountCompletedTasks = []
    maxAmountWithCompletedTasksByUser = max(completedTasksFrequencyByUsers.values())
    for userId, numberOfCompletedTasks in completedTasksFrequencyByUsers.items():
        if numberOfCompletedTasks == maxAmountWithCompletedTasksByUser:
            useridWithMaxAmountCompletedTasks.append(userId)

    return useridWithMaxAmountCompletedTasks

try:
    tasks = r.json()
except json.decoder.decoder.JSONDecodeError:
    print('Mamy błąd strony')
else:
    completedTasksFrequencyByUsers = count_task_frequency(tasks)
    useridWithMaxAmountCompletedTasks = get_users_with_top_tasks(completedTasksFrequencyByUsers)
    print('ID uzytkowników o najwyzszej ilosci wykonanych zadań:', useridWithMaxAmountCompletedTasks)
    
# definicja wyciagania najwiekszej wartości z podanej listy może się przyda
def get_keys_with_top_value(my_dict):
    return [
    key
    for key, value in my_dict.items()
    if value == max(my_dict.values())
    ]

# aby zadziałało wywołanie definicji (wyniku) musi być poniżej wywołania definicji 
# do której sie odwołujesz w anser
anser = get_keys_with_top_value(completedTasksFrequencyByUsers)
print(anser)

'''
# SPOSÓB 1
# znalezienie osoby po imieniu kto otrzymuje ciasteczko

r = requests.get('https://jsonplaceholder.typicode.com/users')

users = r.json()
for user in users:
    if user['id'] in useridWithMaxAmountCompletedTasks:
        print('Imiona osób o najwyższej ilości wykonanych zadań', '\n', user['name'])
        useridWithMaxAmountCompletedTasks.remove(user['id'])
'''

# sposób nr 2
for userId in useridWithMaxAmountCompletedTasks:
    # r = requests.get('https://jsonplaceholder.typicode.com/users/' +str(userId))
    r = requests.get('https://jsonplaceholder.typicode.com/users/', params='id='+str(userId))
    user = r.json()

    print('Wręczamy ciasteczko mistrzunia osoba o imieniu:', '\n', user[0]['name'])
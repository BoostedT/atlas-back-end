#!/usr/bin/python3
"""Using a REST API, for a given employee ID, returns information about his/her
TODO list progress"""

from requests import get
from sys import argv

if __name__ == "__main__":
   response = get('https://jsonplaceholder.typicode.com/todos/')
   data = response.json()
   completed = 0
   total = 0
   tasks = []
   response2 = get('https://jsonplaceholder.typicode.com/users/')
   data2 = response2.json()

for user in data2:
    if user.get('id') == int(argv[1]):
        employee = user.get('name')
    
for task in data:
    if task.get('userId') == int(argv[1]):
        total += 1
        if task.get('completed') is True:
            completed += 1
            tasks.append(task.get('title'))

print("Employee {} is done with tasks({}/{}):".format(employee, completed, total))

for T in tasks:
    print("\t {}".format(T))

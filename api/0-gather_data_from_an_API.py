#!/usr/bin/python3
"""Using a REST API, for a given employee ID, returns information about his/her
TODO list progress"""

import requests

def get_todo_list_progress(employee_id):
    # Fetch the employee's information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    #Send GET request to the URLs
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code == 200 and todos_response.status_code == 200:
        print("Error: Please enter a valid employee ID")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    # extract employee's name
    employee_name = user_data.get('name')

    # count the number of completed and pending tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed') is True]
    number_of_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t " + {task.get('title')})

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_todo_list_progress(employee_id)
        except ValueError:
            print("Error: Please enter a valid employee ID")

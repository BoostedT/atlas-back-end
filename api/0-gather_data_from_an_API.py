#!/usr/bin/python3
""" Fetch employee data and TODO list from a given employee ID """

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """ Fetch employee data and TODO list from a given employee ID """
    try:
        # Fetch employee data
        employee_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        )
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        employee_data = employee_response.json()

        print("Debug: Full Employee Data Fetched:", employee_data)  # Debug line

        # Extract employee name and confirm its presence
        if 'name' in employee_data:
            employee_name = employee_data['name']
        else:
            print("Error: 'name' key not found in employee data.")
            employee_name = "Unknown"

        # Fetch TODO list for the employee
        todos_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        )
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos = todos_response.json()

        # Calculate tasks done and total tasks
        completed_tasks = [task for task in todos if task['completed']]
        total_tasks = len(todos)
        done_tasks_count = len(completed_tasks)

        # Print output in the specified format
        print(
            f"Employee {employee_name} is done with tasks"
            f"({done_tasks_count}/{total_tasks}):"
        )
        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"Unexpected data format: missing key {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")

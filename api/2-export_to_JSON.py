#!/usr/bin/python3
""" Export all employees' TODO data in JSON format """

import json
import requests

if __name__ == "__main__":
    # Base URL for API requests
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users = requests.get(f"{base_url}/users").json()
    data = {}

    # Process each user
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Fetch TODOs for the current user
        todos = requests.get(
            f"{base_url}/todos", params={"userId": user_id}
        ).json()

        # Add user's TODO tasks to data
        data[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            for todo in todos
        ]

    # Write all data to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print("Data exported to todo_all_employees.json")

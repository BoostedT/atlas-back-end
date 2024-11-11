#!/usr/bin/python3
"""extended Export data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    user_dict = {}
    for user in users:
        user_id = user.get("id")
        user_dict[user_id] = []
        for todo in todos:
            if todo.get("userId") == user_id:
                user_dict[user_id].append({
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
                })

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_dict, jsonfile)

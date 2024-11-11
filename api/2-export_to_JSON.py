#!/usr/bin/python3
""" Export data in the JSON format """

import json
import requests

if __name__ == "__main__":
    users = requests.get(
        f"https://jsonplaceholder.typicode.com/users").json()
    data = {}
    for user in users:
        user_id = user.get("id")
        data[user_id] = []
        todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params={"userId": user_id}
        ).json()
        for todo in todos:
            task = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }
            data[user_id].append(task)
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)

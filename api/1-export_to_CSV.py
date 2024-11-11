#!/usr/bin/python3
""" Export data in the CSV format """

import csv
import requests
import sys

if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    rows = []
    
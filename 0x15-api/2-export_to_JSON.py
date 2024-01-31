#!/usr/bin/python3
"""Export to JSON"""
import requests
import sys
import json

if __name__ == "__main__":
    request = requests.Session()
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    url_2 = "https://jsonplaceholder.typicode.com/user/{}/todos".format(
        sys.argv[1])
    user_info = request.get(url_1).json()
    user_tasks = request.get(url_2).json()
    employee_name = user_info["username"]
    user_tasks_json = {}
    for task in user_tasks:
        del task['userId']
        del task['id']
        task["username"] = employee_name
    user_tasks_json[sys.argv[1]] = user_tasks
    with open("{}.json".format(sys.argv[1]), 'w') as f:
        json.dump(user_tasks_json, f)

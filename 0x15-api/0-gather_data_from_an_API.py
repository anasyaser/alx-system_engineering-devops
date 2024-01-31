#!/usr/bin/python3
"""Handle REST API response"""
import requests
import sys

if __name__ == "__main__":
    request = requests.Session()
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    url_2 = "https://jsonplaceholder.typicode.com/user/{}/todos".format(sys.argv[1])
    user_info = request.get(url_1).json()
    user_tasks = request.get(url_2).json()
    completed_tasks = [item['title'] for item in user_tasks if item['completed']]
    employee_name = user_info["name"]
    done_tasks = len(completed_tasks)
    total_tasks = len(user_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))
    print("\t", "\n\t ".join(completed_tasks))

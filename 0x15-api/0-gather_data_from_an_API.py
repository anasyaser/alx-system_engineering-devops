#!/usr/bin/python3
"""Handle REST API response"""
import requests
import sys

if __name__ == "__main__":
    request = requests.Session()
    url_ = "https://jsonplaceholder.typicode.com/{}/todos".format(sys.argv[1])
    response = request.get(url_)
    print("response = {}".format(response.status_code))
    print(response.json())
    print(type(response.json()))
    employee_name = ""
    done_tasks = 0
    total_tasks = 0
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

#!/usr/bin/python3
"""Handle REST API response"""
import requests
import sys

if __name__ == "__main__":
    request = requests.Session()
    url_ = "https://jsonplaceholder.typicode.com/{}".format(sys.argv[1])
    response = request.get(url_)

    employee_name = ""
    done_tasks = 0
    total_tasks = 0
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

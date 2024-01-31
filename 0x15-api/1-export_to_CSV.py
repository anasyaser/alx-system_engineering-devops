#!/usr/bin/python3
"""Export to CSV"""
import requests
import sys

if __name__ == "__main__":
    request = requests.Session()
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    url_2 = "https://jsonplaceholder.typicode.com/user/{}/todos".format(
        sys.argv[1])
    user_info = request.get(url_1).json()
    user_tasks = request.get(url_2).json()
    employee_name = user_info["name"]
    rows = []

    for task in user_tasks:
        rows.append(sys.argv[1] + "," + employee_name + ","
                    + str(task["completed"]) + "," + task["title"])
    with open("{}.csv".format(sys.argv[1]), 'a') as f:
        f.write("\n".join(rows))
        f.write("\n")

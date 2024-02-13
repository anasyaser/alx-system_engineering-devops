#!/usr/bin/python3
"""Fetch api subscripbers for subreddit"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Fetch subreddit subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(sys.argv[1]);

    response = requests.get(url)

    if (response.status_code == 200):
        return response.json().get("data").get("subscribers")
    else:
        return 0

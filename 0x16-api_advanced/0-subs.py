#!/usr/bin/python3
"""
Fetch api subscripbers for subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Fetch subreddit subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(
        url,
        headers={"User-Agent": "Custom"},
    )

    if (response.status_code == 200):
        return response.json().get('data').get("subscribers")
    return 0

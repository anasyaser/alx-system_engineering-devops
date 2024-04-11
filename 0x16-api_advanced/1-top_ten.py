#!/usr/bin/python3
"""
Get the top ten hot posts for given subreddit
"""

import requests


def top_ten(subreddit):
    """print subreddit top ten posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, allow_redirects=False,
                            headers={"User-Agent": "custom"},
                            params={"limit": 10})

    if response.status_code == 200:
        posts = response.json().get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
    else:
        print(None)

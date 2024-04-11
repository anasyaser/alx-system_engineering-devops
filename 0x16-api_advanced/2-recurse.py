#!/usr/bin/python3
"""
Get the all of hot posts recursively
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """print subreddit hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(
        url,
        headers={"User-Agent": "custom"},
        params={"after": after},
    )

    if response.status_code == 200:
        posts = response.json().get("data").get("children")
        for post in posts:
            hot_list.append(post.get("data").get("title"))
        after = response.json().get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
       return

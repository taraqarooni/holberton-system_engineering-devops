#!/usr/bin/python3
"""subscribers"""
import requests


def top_ten(subreddit):
    """ subscribers list"""
    if type(subreddit) is not str:
        print(None)
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-Agent': 'Python3'}
    stre = requests.session()
    stre.headers = headers
    request = stre.get(url, allow_redirects=False)
    if request.status_code == 200:
        results = request.json().get("data")
        [print(c.get("data").get("title")) for c in results.get("children")]
        stre.close()
    else:
        stre.close()
        print(None)

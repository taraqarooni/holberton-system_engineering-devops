#!/usr/bin/python3
"""subscribers"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = "https://www.reddit.com/r/" + subreddit + '/hot.json'
    headers = {'User-Agent': 'Python3'}
    ses = requests.session()
    ses.headers = headers
    param = {'limit': 100, 'after': after}
    request = ses.get(url, params=param)
    if request.status_code == 200:
        after = request.json().get('data').get('after')
        for hot in request.json().get('data').get('children'):
            hot_list.append(hot.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None

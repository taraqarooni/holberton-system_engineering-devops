#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """ subscribers list"""
    # url for get subscribers according to the API
    url = "https://www.reddit.com/r/subreddit/about.json"
    # User-Agent to avoid too many requests 429
    headers = {'user-Agent': 'Python3'}
    # call http and add headers
    request = requests.get(url, params=headers)
    print(request)
    # get the subscribers list
    if request.status_code == 200:
        return request.json().get('data').get('subscribers')
    else:
        return 0

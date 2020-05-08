#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ subscribers list"""
    url = "https://www.reddit.com/r/subreddit/about.json"
    headers = {'user-Agent': 'Python3'}
    stre = requests.session()
    stre.headers = headers
    request = stre.get(url)
    if request.status_code == 200:
        return request.json().get('data').get('subscribers')
    else:
        return 0

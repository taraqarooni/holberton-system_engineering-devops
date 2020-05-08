#!/usr/bin/python3
"""subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ subscribers list"""
    if type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-Agent': 'Python3'}
    stre = requests.session()
    stre.headers = headers
    request = stre.get(url)
    if request.status_code == 200:
        stre.close()
        return request.json().get('data').get('subscribers')
    else:
        stre.close()
        return 0

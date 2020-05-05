#!/usr/bin/python3
#  sends a request to the URL
""" to csv"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'

    reqEmployee = requests.get(url + sys.argv[1])
    reqTodos = requests.get(url + sys.argv[1] + '/todos/')
    jsonemp = reqEmployee.json()
    filename = str(jsonemp.get('id')) + ".csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",",
                               quotechar='"', quoting=csv.QUOTE_ALL)
        for task in reqTodos.json():
            csvwriter.writerow([task.get('userId'), jsonemp.get('username'),
                                task.get('completed'), task.get('title')])

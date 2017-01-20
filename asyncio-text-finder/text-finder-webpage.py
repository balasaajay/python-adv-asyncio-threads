#!/usr/bin/env python
'''
This is a python program for searching for some text in a web page in a traditional way. Works on Python 2.7 and 3+

Installing modules: pip install requests or
                    pip3 install requests
'''

import socket
import urllib
import re
import time
import requests
hosts = ['news.google.com', 'www.facebook.com',
         'www.yahoo.com', 'www.cisco.com', 'www.aol.com']
presidents = ['Bush', 'trump', 'Obama']


def search_news(server):
    url = "https://{}".format(server)

    response = requests.get(url)
    content = response.text

    l = []
    for president in presidents:
        matches = re.findall(president, content)
        for match in matches:
            l.append(match)
    print('server:{} Matches: {}'.format(server, set(l)))

t1 = time.time()
for server in hosts:
    search_news(server)

t2 = time.time() - t1
print("Time taken to run in traditional way in seconds: {}".format(t2))

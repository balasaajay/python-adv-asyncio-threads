#!/usr/bin/env python
'''
This is a python program for searching for some text in a web page in async way. Works on Python 3.5+.
Faster approach.

Install asyncio modules: pip3 install asyncio aiohttp aiosocks

If you have to route your requessts through any socks proxy, uncomment the socks proxy lines and use them.
'''
# import socks
# import socket
import re
import time
import asyncio
import aiohttp
# import aiosocks
# from aiosocks.connector import (
#   SocksConnector, HttpProxyAddr, HttpProxyAuth
# )
tasks = []
# Socks proxy settings
# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'socks.xyz.com', 1000)
# asyncio.socket = socks.socksocket
hosts = ['news.google.com', 'www.facebook.com',
         'www.yahoo.com', 'www.cisco.com', 'www.aol.com']
presidents = ['Bush', 'trump', 'Obama']

async def search_news(server):
#    socks5_addr = aiosocks.Socks5Addr('socks.xyz.com', 1000)
    url = "https://{}".format(server)
#    conn = SocksConnector(proxy=socks5_addr, remote_resolve=True)
    try:
        response = await aiohttp.request('GET', url) 
        # response = await aiohttp.request('GET', url, connector=conn)
        content = await response.read()
        ct=content.decode('utf-8')
    except:
        return
    l=[]
    for president in presidents:
        matches = re.findall(president, ct)
        for match in matches:
            l.append(match)
    print('server:{}  Matches:{}'.format(server, set(l)))

t1 = time.time()
loop = asyncio.get_event_loop()
for server in hosts:
    tasks.append(search_news(server))

loop.run_until_complete(asyncio.wait(tasks))
loop.close()
t2 = time.time() - t1
print("Time taken to run in asyncio way in seconds: {0:.4f}".format(t2))

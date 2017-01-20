# python-adv-asyncio-threads
Advanced python concepts like asyncio, sockets, threads, networking concepts

## 1) clients-chat/

This folder consists of two files: `server.py` and `client.py`

These programs can be started similar to any other python programs: `python filename.py`
 
 Step-1: Start server to listen on port number `18000`
 
 Step-2: In a new terminal window, start client, connect it to the server and enter name
 
 Step-3: In aother terminal window, start another client, connect it to the server and enter a name
 
 Step-4: Clients can now start chatting over the network
 
## 2) threads/

This folder consists of two files: `timer.py` and `async_threads.py`

`timer.py`:  This file uses the concept of synchronous threads, where each thread exits independent of other threads

`async_threads.py`: This file executes thread asynchronously, where one thread waits till the other thread completes 

## 3) asyncio-text-finder/

* Run both the scripts and observe the time taken in each case

`text-finder-webpage.py`: This is a python program for searching for some text in a web page in a traditional way (no threads, no asyncio). ***Slower approach.***

`text-finder-webpage-asyncio.py`: This is a python program for searching for some text in a web page in async way (uses event loops and coroutines) . ***Much Faster approach***

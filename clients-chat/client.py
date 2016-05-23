import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            tLock.release()

host = '127.0.0.1'
port = 0    #picks any free port on computer

server = ('127.0.0.1',18000) #Server started and listening at 18000 (server IP and details)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Define and create a socket
s.bind((host, port)) #Binding socket    
s.setblocking(0) # Make socket as non-blocking 
rT = threading.Thread(target=receving, args=("RecvThread",s))   #receiving thread
rT.start() #Start receiving thread

alias = raw_input("Name: ")
message = raw_input(alias + "-> ")
while message != 'q':
    if message != '':
        s.sendto(alias + ": " + message, server)
    tLock.acquire()
    message = raw_input(alias + "-> ")
    tLock.release()
    time.sleep(0.2)
shudown = True
rT.join()
s.close()

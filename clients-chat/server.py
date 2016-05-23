import socket
import time

host = '127.0.0.1'
port = 18000

clients = [] #to store clients as an array

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP sockets
sock.bind((host,port))
sock.setblocking(0)     #setting socket to non blocking 

quitting = False
print "Server Started."
#repeat the loop until you receive quitting = True 
while not quitting:
    try:
        data, addr = sock.recvfrom(1024)
        if "Quit" in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr) #append client address to 'clients' array
            
        print time.ctime(time.time()) + str(addr) + ": :" + str(data) #To print message in this format
        for client in clients:
            sock.sendto(data, client) #send data to the client
    except:
        pass
sock.close() #close the socket
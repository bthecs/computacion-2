#!/usr/bin/python3
import socket, os, threading, sys

def th_server(sock):
    print("Launching thread...")
    while True:
        msg = sock.recv(1024)
        print("Recibido: %s" % msg.decode())
        if not msg:
            break
#    sock.close()

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = ""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    th = threading.Thread(target=th_server, args=(clientsocket,))
    th.start()
clientsocket.close()

#!/usr/bin/python3
import sys, socket, os

# create a socket object
try:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print ('Fallo al crear el socket!')
    sys.exit()

# get local machine name
host = ""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()
    print('Conexion establecida: SERVER ON')
    child_pid = os.fork()
    if not child_pid:
        while True:
            msg = clientsocket.recv(1024)
            print("Recibido: %s" % (msg.decode()))
            if not msg:
                break
        clientsocket.close()

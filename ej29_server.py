#!/usr/bin/python3
import os
import socket
import sys
import threading
import time
import getopt

(opcion, arg) = getopt.getopt(sys.argv[1:], 'p:')

for (op, ar) in opcion:
    if op == '-p':
        p = int(ar)
        print('Opcion -p exitosa!')


def th_server(sock):
    print("Iniciando thread...\n")
    while True:

        opcion = sock.recv(1024)
        print('Cliente %s:%s' % (addr[0], addr[1]))
        print("Opcion: " + opcion.decode() + '\n')

        if (opcion.decode() == 'ABRIR'):
            texto = '\nNombre del archivo:'
            sock.send(texto.encode())
            archivo = sock.recv(1024).decode()
            fd = open(archivo, 'a+')

        elif (opcion.decode() == 'AGREGAR'):
            fd = open(archivo, 'a+')
            texto = '\n*** Escribir "quit" para terminar ***\nTexto:'
            sock.send(texto.encode())
            while True:
                message = sock.recv(1024)
                if message.decode() == 'quit':
                    break
                print('Recibido: ' + message.decode())
                fd.write(message.decode() + '\n')
            print('Bucle terminado.')
            fd.close()

        elif (opcion.decode() == 'LEER'):
            fd = open(archivo, 'r')
            print('\nEnviando archivo al cliente: ' + archivo + '\n')
            contenido = fd.read()
            sock.sendall(contenido.encode())
            fd.close()

        elif (opcion.decode() == 'CERRAR'):
            fd.close()
            break

        else:
            print('\nOpcion invalida!\n')


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = p

serversocket.bind((host, port))

serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    print("\nObteniendo conexion desde %s:%s\n" % (addr[0], addr[1]))
    th = threading.Thread(target=th_server, args=(clientsocket,))
    th.start()
clientsocket.close()

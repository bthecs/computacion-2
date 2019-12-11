#!/usr/bin/python3
import socket
import sys
import os
import getopt
import time

(opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')

for (op, ar) in opt:
    if op == '-a':
        a = str(ar)
    elif op == '-p':
        p = int(ar)
        print('Opcion -p exitosa!')

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Fallo al crear el socket!')
    sys.exit()

print('Socket Creado!')

host = a
port = p

client.connect((host, port))

print('Socket conectado al host', host, 'en el puerto', port)

while True:

    print("""\n
    \t\t\t *** Menu ***
    - ABRIR
    - AGREGAR
    - LEER
    - CERRAR
    """)

    opcion = input('Opcion: ').upper()

    client.sendto(opcion.encode(), (host, port))

    if (opcion == 'ABRIR'):
        directorio = 'tmp/'
        try:
            os.stat(directorio)
        except:
            os.mkdir(directorio)
        print(client.recv(1024).decode())
        data = input()
        archivo = 'tmp/' + data + '.txt'
        client.sendto(archivo.encode(), (host, port))

    elif (opcion == 'AGREGAR'):
        print(client.recv(1024).decode())
        while True:
            msg = input()
            client.sendto(msg.encode(), (host, port))
            if msg == 'quit':
                break

    elif (opcion == 'LEER'):
        contenido = client.recv(1024).decode()
        print('\nArchivo: ' + archivo + '\n')
        print(contenido)
        input('Apretar Enter...')

    elif (opcion == 'CERRAR'):
        break

    else:
        print('\nOpcion invalida!\n')
        input('Apretar Enter...')

client.close()

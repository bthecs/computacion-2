
import socket, getopt, time, sys, os
(opt,arg) = getopt.getopt(sys.argv[1:], 'a:p:')

print('opciones: ', opt)

a = ""
p = ""

for (op,ar) in opt:
    if (op == '-a'):
        a = ar
        print('Opcion -p exitosa!')
    elif (op == '-p'):
        p = int(ar)
        print('Opcion -f exitosa!')
    else:
        print('Opcion incorrecta!')

#create dgram udp socket
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error:
    print('Error al crear el socket')
    sys.exit()

host = a
port = p

while True:
    msg = input('Ingrese msg: ').encode()
    try:
        s.sendto(msg, (host, port))
    except socket.error:
        print('Error Code: ' + str(msg[0]) + 'Message' + msg[1])
        sys.exit()

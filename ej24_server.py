import socket, sys, time, getopt, os

(opt,arg) = getopt.getopt(sys.argv[1:], 'p:f:')

print('opciones: ', opt)

p = ""
f = ""

for (op,ar) in opt:
    if (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')
    elif (op == '-f'):
        f = ('tmp/'+ar)
        print('Opcion -f exitosa!')
    else:
        print('Opcion incorrecta!')

#create a socket object
serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = ""
port = p

serversocket.bind((host, port))

fd = open(f,"w+")

while True:
    data,addr = serversocket.recvfrom(1024)
    print(addr)
    address = addr[0]
    port = addr[1]
    print('Address: %s - Port: %d' %(address, port))
    print('Recibido: '+data.decode('ascii'))
    fd.write('\n'+data.decode('ascii'))
    time.sleep(1)

clientsocket.close()

import socket,sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = str(sys.argv[1])
port = int(sys.argv[2])

s.connect((host, port))

while True:
    msg = input('Ingrese msg: ').encode()
    if msg.decode() == 'exit':
        sys.exit()
    else:
        try:
            s.sendto(msg, (host, port))
        except socket.error:
            print('Error Code: ' + str(msg[0]) + 'Message' + msg[1])
            sys.exit()
s.close()

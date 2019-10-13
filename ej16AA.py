import os, time

nombreuser = "userAA"
pipe_name = "chat"

if __name__ == '__main__':
    encoding = 'utf-8'
    if not os.path.exists(pipe_name):
        os.mkfifo(pipe_name)
    fd = os.open(pipe_name, os.O_RDWR)
    while True:
        print(str(os.read(fd, 30), 'utf-8'))
        linea = input("\nIngrese su mensaje: ")
        linea = nombreuser + ": " + linea
        linea = str.encode(linea)
        os.write(fd, linea)
        time.sleep(1)

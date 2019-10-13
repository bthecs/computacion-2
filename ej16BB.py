import os, time

nombreuser = "userBB"
pipe_name = "chat"

if __name__ == '__main__':
    fd = os.open(pipe_name, os.O_RDWR)
    while True:
        linea = input("\nIngrese su mensaje: ")
        linea = nombreuser + ": " + linea
        linea = str.encode(linea)
        os.write(fd, linea)
        time.sleep(1)
        print(str(os.read(fd, 30), 'utf-8'))
    os.close()

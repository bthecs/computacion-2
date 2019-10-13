import os,sys,time
from multiprocessing import Process,Pipe

fifo='/tmp/pipe_test'

def main():
    fifo_fd=open(Fifo,"r")
    line = fifo_fd.readline()
    lector_conn, escritor_conn = Pipe()
    pid = Process(target=hijo,args=(lector_conn, ))
    pid.start()
    escritor_conn.send(line)
    escritor_conn.close()
    time.sleep(4)
    pid.join()
    pid.close()
    sys.exit(0)

def hijo(lector_conn):
    time.sleep(1)
    print("El mensaje recibido es: ",lector_conn.recv())
    sys.exit(0)

if __name__ == '__main__':
    main()

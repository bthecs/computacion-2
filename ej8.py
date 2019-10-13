import os
import time
import signal
import multiprocessing
from multiprocessing import Process


#Manejo de seÃ±ales
def handler(signum,frame):
    return


#Registro de seÃ±ales
signal.signal(signal.SIGUSR1,handler)


#Subproceso - Hijo 1
def child1(pid_p):
    while True:
        print('-----------------------------------------')
        print('Soy proceso Hijo 1 con PID=%s: "ping" ' %(os.getpid()))
        os.kill(pid_p,signal.SIGUSR1)
        time.sleep(5)


#Subproceso - Hijo 2
def child2():
    while True:
        print('Soy proceso Hijo 2 con PID=%s: "pong" ' %(os.getpid()))
        print('-----------------------------------------')
        signal.pause()


#Proceso - Padre
if __name__ == '__main__':
    pid_p=os.getpid()
    p1=Process(target=child1, args=(pid_p,))
    p2=Process(target=child2)
    p1.start()
    p2.start()
#Bucle de la seÃ±al
    while True:
        os.kill(p2.pid, signal.SIGUSR1)
        signal.pause()

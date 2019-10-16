from multiprocessing import Queue, Lock
import threading
import time
import os
import multiprocessing

def thread_function(x,l,q):
    l.acquire()
    time.sleep(x)
    q.put("mi PID es: %d,Nombre: %s, Thread %d,Proceso: %d"%(os.getpid(),threading.current_thread().getName(),threading.get_ident(),x))
    l.release()

def mostrarCola(q):
    while True:
        print(q.get())
        if q.empty():
            break

if __name__ == "__main__":
    q = Queue()
    l = Lock()

    p=[]
    for x in range(10):
        p.append(threading.Thread(target=thread_function, args=(x,l,q)))
        p[x].start()

    for x in range(10):
        p[x].join()
    mostrarCola(q)
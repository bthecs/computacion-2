from multiprocessing import Queue, Lock
import threading
import time
import os



def thread_function(x,l,q):
    l.acquire()
    time.sleep(1)
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
    pid=os.getpid()

    for x in range(3):
        p1 = threading.Thread(target=thread_function, args=(x,l,q))
        p1.start()
        time.sleep(1)
        p1.join()
    mostrarCola(q)
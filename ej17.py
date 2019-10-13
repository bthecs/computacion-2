from multiprocessing import Lock, Queue
import time
import os
import multiprocessing

def f(l, n,q):
    l.acquire()
    time.sleep(n)
    q.put ("Process: %d PID: %d" % (n,os.getpid()))
    l.release()

def mostrarCola(q):
    while True:
        print(q.get())
        if q.empty():
            break

if __name__ == '__main__':
    q = Queue()
    lock = Lock()

    for num in range(10):
        pid = os.fork()
        if pid == 0:
            f(lock, num,q)

    mostrarCola(q)

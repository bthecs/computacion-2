from multiprocessing import Queue, Pool
import os, time

def f(x):
    time.sleep(1)
    q.put("Proceso: %d PID: %d" % (x, os.getpid()))

def mostrarCola():
    while True:
        print(q.get())
        if q.empty():
            break

q = Queue()

if __name__ == '__main__':
    p = Pool(processes=10)
    p.map(f, range(10))
    mostrarCola()

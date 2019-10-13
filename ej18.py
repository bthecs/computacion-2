from multiprocessing import Process, Queue, Lock
import os, time

def f(x,l,q):
    l.acquire()
    # Esperar 'x' segundos
    time.sleep(x)
    # Introducir msg a la cola
    q.put("Proceso: %d PID: %d" % (x, os.getpid()))
    l.release()

#Funcion 'Cola'
def mostrarCola(q):

    while True:
        # Imprime la cola
        print(q.get())
        # Si la cola esta vacia, sale del While
        if q.empty():
            break

#Proceso 'Padre'
if __name__ == '__main__':
    # Definir la cola
    q = Queue()
    # 'Lock' para sincronizar los procesos
    lock = Lock()
    # 'For' para iniciar 10 procesos
    for x in range(10):
    # Definir proceso
        p = Process(target=f, args=(x,lock,q))
        p.start()
    # Esperar a que el proceso termine
        p.join()
    # Iniciar la funcion para imprimir la cola
    mostrarCola(q)

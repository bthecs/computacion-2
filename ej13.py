import os
import multiprocessing
import time
from multiprocessing import Process

#Hijo1
def child1(x):
    print("PID Hijo1: ", os.getpid(), "PID Padre: ", x)
    time.sleep(1)

#Hijo2
def child2(x):
    print("PID Hijo2: ", os.getpid(), "PID Padre: ", x)
    time.sleep(1)

#Hijo3
def child3(x):
    print("PID Hijo2: ", os.getpid(), "PID Padre: ", x)
    time.sleep(1)

#Padre
if __name__ == '__main__':
    pid=os.getpid()
    p1=Process(target=child1, args=(pid,))
    p2=Process(target=child2, args=(pid,))
    p3=Process(target=child3, args=(pid,))
    print("Lanzando Hijo1")
    p1.start()
    p1.join()
    print("Lanzando Hijo2")
    p2.start()
    p2.join()
    print("Lanzando Hijo3")
    p3.start()
    p3.join()

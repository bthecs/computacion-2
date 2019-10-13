import os, sys, time, multiprocessing
from multiprocessing import Process, Pipe

def child1(a):
    sys.stdin = open(0)
    while True:
        #print(sys.stdin)
        print('Ingrese una linea: ')
        print('Ingrese una linea: ')
        c = sys.stdin.readline()
        a.send(c)
        time.sleep(.3)

def child2(b):
    while True:
        print('\nLeyendo', '(PID:', os.getpid(), '):', b.recv())


if __name__ == '__main__':
    a, b = Pipe()
    p1=Process(target=child1, args=(a,))
    p2=Process(target=child2, args=(b,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

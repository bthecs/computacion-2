import os

def child():
    for x in range(5):
        print("Soy Hijo %d" %(os.getpid()))
    os._exit(0)

def parent():
    childProc = os.fork()
    if childProc == 0:
        child()
    else:
        childExit = os.wait()
        print("Mi proceso hijo %d termino." %(childExit[0]))
        for x in range(2):
            print("Soy Padre %d" %(os.getpid()))

parent()

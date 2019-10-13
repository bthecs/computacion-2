import os

def child(x):
    print("Soy el proceso %d. Mi padre es %d" %(os.getpid(), x))
    os._exit(0)


def parent():
    print("Padre:", os.getpid())
    pid = os.getpid()
    for x in range(3):
        childProc = os.fork()
        if childProc == 0:
            child(pid)

parent()

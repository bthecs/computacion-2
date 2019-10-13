import os
import sys
import time
import signal

def handler(signum,frame):
    return

signal.signal(signal.SIGUSR1,handler)
signal.signal(signal.SIGUSR2,handler)

def main():
    #Proceso A
    r, w = os.pipe()
    print("Proceso A")
    A = os.getpid()
    B = os.fork()

    if B == 0:
        #Proceso B
        signal.pause()
        print("Proceso B")
        os.close(r)
        w = os.fdopen(w,'w')
        w.write("Mensaje 1 (PID:%s)\n" %os.getpid())
        w.flush()
        time.sleep(.3)
        C = os.fork()
        os.kill(C,signal.SIGUSR1)
        os.wait()
        os._exit(0)

        if C == 0:
            #Proceso C
            signal.pause()
            print("Proceso C")
            w.write("Mensaje 2 (PID:%s)\n" %os.getpid())
            w.close()

            os.kill(A,signal.SIGUSR2)
            time.sleep(.3)
            os._exit(0)

    time.sleep(.3)
    os.kill(B,signal.SIGUSR1)
    signal.pause()
    r = os.fdopen(r, 'r')
    for line in r:
        print("%s"%line)
    r.close()

main()

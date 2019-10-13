import os
import sys
import time


def main():
    r, w = os.pipe()
    processid = os.fork()
    if processid:
        print("Proceso padre")

    if processid == 0:
        os.close(r)
        w = os.fdopen(w,'w')
        print("Escribir mensaje:")
        for line in sys.stdin:
            w.write("%s" % line)
            w.flush()
        sys.exit(0)

    pid2 = os.fork()

    if pid2 == 0:
        time.sleep(3)
        os.close(w)
        r = os.fdopen(r)
        for line in r:
            print("---Segundo proceso hijo---")
            print("PID: %d" % os.getpid())
            print("Mensaje:")
            print("%s" % line)
        sys.exit(0)

    os.wait()
    os.wait()

main()

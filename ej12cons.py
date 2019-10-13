import os

def msgFifo():
    fd = open("Fifo","r")
    mensaje = fd.readline()
    mensaje = str(mensaje)
    fd.close()
    return mensaje

def Hijo(r):
    os.close(w)
    r = os.fdopen(r, "r")
    linea = r.readline()
    print("El mensaje recibido es: %s" % linea)
    r.close()

r, w = os.pipe()

pid = os.fork()

if pid:
    os.close(r)
    w = os.fdopen(w, 'w')
    w.write(msgFifo())
    w.close()
else:
    Hijo(r)

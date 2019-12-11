"""Ejercicio 21 â Threading / Pipe / FIFO
Reescribir el programa consumidor del ejercicio 15 para que haga uso de
multithreading."""
import os,sys,time


fifo= '/tmp/pipe_test'
def productor():
    fifo_fd = open(fifo,"w")
    print("Proceso padre")
    fifo_fd.write(sys.argv[1]+"\n")
    time.sleep(1)
if not os.path.exists(fifo):
    os.mkfifo(fifo)

productor()
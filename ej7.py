import os
import time
import signal

#Hijo.
def child():
    print('Hijo:','Iniciando...')
    while True:
        print(,'Hijo:','SeÃ±al recibida!')
        signal.pause()

#Manejo de seÃ±ales.
def handler(signum,frame):
    print('Padre:','Mandando seÃ±al...')
    return

#Registro de seÃ±ales.
signal.signal(signal.SIGUSR1, handler)

#Creando fork.
pid = os.fork()

if pid == 0:
    child()
#Padre.
else:
    print('Padre:','Iniciando...')
    while True:
        os.kill(pid,signal.SIGUSR1)
        time.sleep(5)

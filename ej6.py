import signal
import os
import time


def handler(s,f):
    print('\nEsta vez me saldrÃ©, intÃ©ntalo nuevamente')
    signal.signal(signal.SIGINT, signal.SIG_DFL)


#Registro de seÃ±ales
signal.signal(signal.SIGINT, handler)


#Tiempo para apretar 'Ctrl + C'
time.sleep(100)

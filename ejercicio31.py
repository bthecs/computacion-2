import sys
import getopt
import threading
import string
import time
(opt,arg)=getopt.getopt(sys.argv[1:],'f:r:',["archivo","iteraciones"])


def f(lock,file_name,n,letra):
    lock.acquire()
    file = open(file_name, 'a')
    for i in range(n):
        file.write(letra)
    time.sleep(1)
    file.close()
    lock.release()


if __name__=="__main__":
    for (op, ar) in opt:
        if (op in ['-f', 'archivo']):
            nombre_archivo=ar
        if (op in ['-r', 'iteraciones']):
            cant_iteraciones = int(ar)
    lock=threading.Lock()
    letras = string.ascii_uppercase
    try:
        aux=open(nombre_archivo,'r+')
        contenido=aux.read()
        if contenido!='':
            aux.seek(0)
            aux.truncate() #Borramos el contenido del archivo solo si este fue escrito anteriormente
        aux.close()
    except FileNotFoundError as e:
        file=open(nombre_archivo,'a')
        file.close()
    lista=[]
    for i in range(15):
        letra=letras[i]
        lista.append(threading.Thread(target=f,args=(lock,nombre_archivo,cant_iteraciones,letra)))
        lista[i].start()
    for i in lista:
        i.join()
    print("El nombre del archivo es:",nombre_archivo)
    print("La cantidad de iteraciones es:",cant_iteraciones)
    print("El contenido de las iteraciones es:",contenido)
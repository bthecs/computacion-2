import getopt, sys, os, time, math
from multiprocessing import Pool

(opt,arg) = getopt.getopt(sys.argv[1:], 'n:m:')

print('opciones: ', opt)

n = ""
m = ""

for (op,ar) in opt:
    if (op == '-n'):
        n = int(ar)
        print('Opcion "n" seteada!')
    elif (op == '-m'):
        m = int(ar)
        print('Opcion "m" seteada!')
    else:
        print('Opcion invalida.')

def raiz(num):
    if (num % 2 != 0):
        raiz = math.sqrt(num)
        print('La Raiz de',num,'es:',raiz)
        return raiz

pool = Pool()
for x in range(n, m, 1):
    pool.apply(raiz,args=(x,))

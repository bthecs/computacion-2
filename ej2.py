import getopt
import os.path
import sys

(opt, arg) = getopt.getopt(sys.argv[1:], 'i:o:', ['tmp1=', 'tmp2='])

print('Opciones: ', opt)
print('Argumentos ', arg)

for (op, ar) in opt:
    if op == '-i':
        file1 = str(ar)
    elif op == '-o':
        file2 = str(ar)

if os.path.isfile(file1):
    file1 = open(file1, 'r')
    file2 = open(file2, '+w')
    linea = file1.readline()
    while linea:
        file2.write(linea)
        linea = file1.readline()

#python3 ej2.py -i tmp/file1 -o tmp/file2

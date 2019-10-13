import getopt
import sys

(opt, arg) = getopt.getopt(sys.argv[1:], 'o:n:m:', ['opcion=', 'num1=', 'num2='])

print('Opciones: ', opt)
print('Argumentos ', arg)

operador = ''
num1 = ''
num2 = ''

for (op, ar) in opt:
    if (op == '-o'):
        if (ar == '+'):
            operador = ar
        elif (ar == '-'):
            operador = ar
        elif (ar == '*'):
            operador = ar
        elif (ar == '/'):
            operador = ar

    if (op == '-n'):
        num1 = int(ar)

    if (op == '-m'):
        num2 = int(ar)

print('\n\nResultado:\n')

if operador == '+':
    print('\t%d + %d = %d\n' % (num1, num2, num1 + num2))
elif operador == '-':
    print('\t%d - %d = %d\n' % (num1, num2, num1 - num2))
elif operador == '*':
    print('\t%d * %d = %d\n' % (num1, num2, num1 * num2))
elif operador == '/':
    print('\t%d / %d = %d\n' % (num1, num2, num1 / num2))
else:
    print('\tError!\n')

#python3 ej1.py -o '+' -n 5 -m 5

import getopt, sys, os

(opt,arg) = getopt.getopt(sys.argv[1:], 'a:')

arg = ""

for (op,ar) in opt:
    if(op == '-a'):
        arg = ar
        arg = str(arg)

fd = open("Fifo","w")

fd.write(arg)

fd.close()

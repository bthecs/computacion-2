import os

def child(num):
    print("\n#El hijo decrementa el numero en 2.")
    print("Hijo:", num - 2)  # El Hijo incrementa el numero en 2
    os._exit(0)

def parent():
    num = int(input("Ingrese numero: "))
    childProc = os.fork()
    if childProc == 0:
        child(num)
    else:
        print("\n#El padre incrementa el numero en 4.")
        print("Padre:", num + 4)  # El Padre incrementa el numero en 4

parent()

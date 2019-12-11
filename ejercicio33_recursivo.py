from concurrent.futures import ThreadPoolExecutor
import sys
import getopt
(opt,arg)=getopt.getopt(sys.argv[1:],'n:m:',["numero1","numero2"])
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

if __name__=="__main__":
    for (op,ar) in opt:
        if (op in ['-n', 'numero1']):
            n=int(ar)
        if (op in ['-m', 'numero2']):
            m=int(ar)

    resta=m-n
    pool=ThreadPoolExecutor(resta)
    print("Ingrese -n como parametro mas pequeÃ±o.")
    while(n<m):
        for i in range(n):
            future=pool.submit(recur_fibo,n)
        n+=1
        print(future.result())
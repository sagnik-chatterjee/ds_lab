'''
map reduce for pi 
'''
import sys 

def integral(x):
    return 4.0/(1.0+x*x)
for line in sys.stdin:
    line=line.strip()
    words=line.split()
    n=int(words[0])
    delx = 1.0/n 
    for i in range(0,n):
        print("1\t%1.10f" %(integral(i*delx)*delx))

        

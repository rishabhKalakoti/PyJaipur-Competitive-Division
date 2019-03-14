#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def gcd(a,b): 
      
    # Everything divides 0  
    if (b == 0): 
         return a 
    return gcd(b, a%b) 

def getTotalX(a, b):
    g = b[0]
    for i in range(1,len(b)):
        g=gcd(g,b[i])
    l = a[0]
    for i in range(1,len(a)):
        l = (l*a[i])/gcd(l,a[i])
    if(g%l != 0):
        return 0
    i=0
    x=l
    while(g>=x):
        if(g%x==0):
            i+=1
        x+=l
    return i

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

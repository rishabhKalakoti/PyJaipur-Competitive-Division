#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    ans = 0
    p = len(c)-1
    while(p>0):
        if(p-2 >=0 and c[p-2]==0):
            p = p-2
            ans += 1
        else:
            p = p-1
            ans += 1
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

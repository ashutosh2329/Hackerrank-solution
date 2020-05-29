#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    d = 0
    i = 0
    while(i<n):
        c = 1
        for j in range(i+1,len(ar)):
            if(ar[i] == ar[j]):
                c += 1
            else:
                break
        d += int(c/2)
        i += c  

    return d
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

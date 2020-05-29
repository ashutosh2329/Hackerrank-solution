#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    m = 0
    v = 0
    d = 0
    for i in s:
        if(i=='U'):
            v -= 1
        else:
            v += 1 
        if(v == 0 and i == 'U'):
            d += 1
    return d
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

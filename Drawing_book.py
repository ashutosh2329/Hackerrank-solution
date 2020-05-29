#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.

    if(p>n/2):
        if(p==n-1 and n%2==0):
            return(1)
        return(int((n-p)/2))
    else:
        return(int(p/2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

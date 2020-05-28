import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]
    c_low = 0
    c_high = 0
    lis = []
    for i in range(len(scores)):
        if(scores[i]<lowest):
            c_low += 1
            lowest = scores[i]
        if(scores[i]>highest):
            c_high += 1 
            highest = scores[i]

    lis.append(c_high)
    lis.append(c_low)
    return lis
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.

def kangaroo(x1, v1, x2, v2):
    result = 'NO'
    if(x1<=x2 and v1>v2):
        while((x1+v1)<=(x2+v2)):
            if(x1+v1 == x2+v2):
                result = 'YES'
                break
            print(x2)
            x1 += v1
            x2 += v2
    elif(x2<=x1 and v2>v1):
        while((x1+v1)>=(x2+v2)):
            if(x1+v1 == x2+v2):
                result = 'YES'
                break
            x1 += v1
            x2 += v2
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

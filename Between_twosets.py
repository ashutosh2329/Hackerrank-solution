import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def find_gcd(x,y):
    while(y):
        x,y = y,x%y
    
    return x

def find_fact(gcd):
    lis = []
    for i in range(1,int(gcd/2+1)):
        if(gcd%i == 0):
            lis.append(i)
    return lis

def getTotalX(a, b):
    c =0
    num1=b[0]
    if(len(b)<2):
        num2=0
    else:
        num2=b[1] 
    gcd=find_gcd(num1,num2) 
    for i in range(2,len(b)): 
        gcd=find_gcd(gcd,b[i])
    lis = find_fact(gcd)
    lis.append(gcd)




    for i in range(len(lis)):
        flag = True
        for j in range(len(a)):
            if(lis[i]%a[j]!=0):
                flag=False
                break
        if(flag):
            c += 1

    return c




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

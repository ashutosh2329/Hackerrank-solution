import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0
    min = arr[1]
    max = 0
    for i in range(len(arr)):
        if(arr[i]<min):
            min = arr[i]
        elif(arr[i]>max):
            max = arr[i]
        sum += arr[i]
    print(f"{sum-max} {sum-min}")
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


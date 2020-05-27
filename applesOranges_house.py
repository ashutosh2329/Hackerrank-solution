import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    c = 0
    for i in range(len(apples)):
        apples[i] += a
        if(apples[i]>=s and apples[i]<=t):
            c += 1
    print(c)
    c = 0
    for i in range(len(oranges)):
        oranges[i] += b
        if(oranges[i]>=s and oranges[i]<=t):
            c += 1
    print(c)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

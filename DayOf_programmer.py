#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    string = ''
    if(year>1918):
        if(year%400 == 0):
            string = '12.09.' + str(year)
        elif(year%4 ==0 and year%100 != 0):
            string = '12.09.' + str(year)
        else:
            string = '13.09.' + str(year)
    elif(year<1918):
        if(year%4 == 0):
            string = '12.09.' + str(year)
        else:
            string = '13.09.' + str(year)
    else:
        string = '26.09.' + str(year)

    return string



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

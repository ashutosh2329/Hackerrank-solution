# import math
# import os
# import random
# import re
# import sys

# # Complete the miniMaxSum function below.
# def miniMaxSum(arr):
#     max_sum = 0
#     min_sum = 0
#     arr.sort()
#     for i in range(len(arr)-1):
#         min_sum += arr[i]
#     arr.sort(reverse = True)
#     for i in range(len(arr)-1):
#         max_sum += arr[i]
#     print(f"{min_sum} {max_sum}")
# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)

# import math
# import os
# import random
# import re
# import sys

# # Complete the formingMagicSquare function below.
# def formingMagicSquare(s):
#     diffs = []
#     all_possible = [
#                 [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
#                 [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
#                 [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
#                 [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
#                 [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
#                 [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
#                 [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
#                 [[2, 7, 6], [9, 5, 1], [4, 3, 8]],]

#     #compare s to each in all possible get number of differences for each to diffs
#     for possiblity in all_possible:
#         total_cost = 0
#         for p_row, s_row in list(zip(possiblity,s)):
#             for p_num, s_num in (list(zip(p_row, s_row))):
#                 if p_num != s_num:
#                     total_cost += abs(p_num - s_num)
#         diffs.append(total_cost)
#     temp = diffs[1]
#     for i in range(len(diffs)):
#         if(diffs[i]<temp):
#             temp = diffs[i]
#     return temp

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = []

#     for _ in range(3):
#         s.append(list(map(int, input().rstrip().split())))

#     result = formingMagicSquare(s)

#     fptr.write(str(result) + '\n')

#     fptr.close()
#This solution gives 100% accuracy

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    length_arr = len(arr)
    summer_1 = 0
    summer_2 = 0
    indx = length_arr
    for i in range(length_arr):
        summer_1 += arr[i][i]
        summer_2 += arr[i][indx-i-1]
        
    return abs(summer_1-summer_2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

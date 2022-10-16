#This xolution gives 100% accuracy

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_arr = min(arr)
    max_arr = max(arr)
    
    max_max = sum(arr)-min_arr
    min_max = sum(arr)-max_arr
    
    print(min_max,max_max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

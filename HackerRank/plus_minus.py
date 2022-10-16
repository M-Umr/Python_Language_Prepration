#This solution gives 100% accuracy

#!/bin/python3

import math
import os
import random
import re
import sys
import decimal
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    length_arr = len(arr)
    positive_num_length = len(list(filter(lambda x: x>0,arr)))
    negative_num_length = len(list(filter(lambda x: x<0,arr)))
    zero_num_length = len(list(filter(lambda x: x==0,arr)))
    positive_result = decimal.Decimal(positive_num_length)/decimal.Decimal(length_arr)
    positive_result = round(positive_result,6)
    negative_result = decimal.Decimal(negative_num_length)/decimal.Decimal(length_arr)
    negative_result = round(negative_result,6)
    zero_result = decimal.Decimal(zero_num_length)/decimal.Decimal(length_arr)
    zero_result = round(zero_result,6)
    print(positive_result)
    print(negative_result)
    print(zero_result)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

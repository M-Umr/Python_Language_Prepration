#This solution gives 100% accuracy

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    result = [k for k,v in Counter(a).items() if v == 1]
    return int(result[0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    
    fptr.write(str(result) + '\n')

    fptr.close()

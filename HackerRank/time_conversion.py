#This solution gives 100% accuracy

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import *
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    m2 = datetime.strptime(s, '%I:%M:%S%p')
    re_str = str(m2)
    result = re_str.split(' ')
    return result[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    
    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

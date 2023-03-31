#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    positive = sum(x > 0 for x in arr)
    negative = sum(x < 0 for x in arr)
    zero = sum(x == 0 for x in arr)
    print("{:.6f}".format(positive/n))
    print("{:.6f}".format(negative/n))
    print("{:.6f}".format(zero/n))
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

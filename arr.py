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
    print("Percentage of positive integers : {:.6f}".format(positive/n))
    print("Percentage of negative integers : {:.6f}".format(negative/n))
    print("Percentage of zero integers : {:.6f}".format(zero/n))
            
if __name__ == '__main__':

    arr = list(map(int, input('Enter the integers separated by a coma : ').rstrip().split(',')))

    plusMinus(arr)



#!/bin/python3

import math
import os
import random
import re
import sys


"""
We define super digit an integer x using the following rules: given an integer, we need to find the super digit of the integer. 
if x has only 1 digit, then its super digit is x. 
Otherwise, the super digit of x is equal to the super digit of the sume of digits of x.
functions description: superDigit has the following params:
string n : a string representation of an integer. 
int k : the times to concatenate n to make p. 
Returns- int: the super digit of n repeated k times. Constraints: 1<= n < 10^100000, 1<= k <= 10^5
"""
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    def digitSum(x):
        if len(x) == 1:
            return int(x)
        else:
            return digitSum(str(sum(int(d) for d in x)))
    super_digit = digitSum(n)*k
    return digitSum(str(super_digit))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

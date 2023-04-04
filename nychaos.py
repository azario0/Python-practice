#!/bin/python3

import math
import os
import random
import re
import sys


"""
Determine the minimum number of bribes that took place to get to a given queue order. print the number of bribes, or , if anyone has bribed more tan two, print `Too chaotic`. 
function description: minimumBribes has the following params: 
int q[n]: the positions of the people after all bribes.
Returns- No value is returned. 
Print the minimum number of bribes necessary or `Too chaotic` if someone has bribed more than 2 people.
Constraints: 1<= t <=10, 1<=n<10^5. subtasks for  60% score 1<=n<=10^3, for 100% score 1<=n<10^5
"""

# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i+1)>2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i]-2),i):
            if q[j]>q[i]:
                bribes +=1
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

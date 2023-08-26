"""
This problem requires you to check if a given string of brackets is balanced or not. A string is considered balanced if all the opening brackets have corresponding closing brackets and they are in the correct order.

Here's the algorithm to solve this problem:

Create an empty stack to store opening brackets
For each bracket in the string:
a. If it's an opening bracket, push it onto the stack
b. If it's a closing bracket:
i. If the stack is empty, return "NO" (the string is not balanced)
ii. If the top of the stack is not the corresponding opening bracket, return "NO"
iii. If the top of the stack is the corresponding opening bracket, pop it off the stack
If the stack is empty, return "YES" (the string is balanced), otherwise return "NO"
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def is_balanced(s):
    stack = []
    for bracket in s:
        if bracket in ['(', '{', '[']:
            stack.append(bracket)
        else:
            if not stack:
                return "NO"
            top = stack.pop()
            if (bracket == ')' and top != '(') or \
               (bracket == '}' and top != '{') or \
               (bracket == ']' and top != '['):
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input('Enter a string containing {} , [] or () in any order you want : ')

        result = is_balanced(s)

        fptr.write(result + '\n')

    fptr.close()

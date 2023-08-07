"""
You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format

The first line contains integer T, the number of test cases.
The next T lines contains the string S.

Constraints
0 < T < 100
"""
import re
def is_valid_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False
if __name__ == '__main__':
    for _ in range(int(input())):
            print(is_valid_regex(input()))
"""
This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. 
So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
Task

You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.

Constraints
0 < k <= len(S)
"""
from itertools import combinations_with_replacement

def main():
    s, k = input().split()
    k = int(k)
    s = sorted(s)
    for i in combinations_with_replacement(s, k):
        print(''.join(i))

if __name__ == '__main__':
    main()
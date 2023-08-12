"""
Task

You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.

Constraints
0 < k <= len(S)
the string contains only UPPERCASE characters.
"""
from itertools import combinations

def print_combinations(string, k):
    for i in range(1, k + 1):
        for j in combinations(sorted(string), i):
            print(''.join(j))

if __name__ == '__main__':
    string, k = input().split()
    print_combinations(string, int(k))
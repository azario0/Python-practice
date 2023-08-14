"""
Problem Statement: Maximize It
You are given k lists of integers, each with n elements. 
You need to choose one element 
from each list such that the sum of the squares of the chosen elements is maximized, 
subject to the constraint that the sum modulo m is less than or equal to a given integer M.
"""
from itertools import product

if __name__ == '__main__':
    k,m = map(int, input().split())
    lists = []
    for _ in range(k):
        lst = list(map(int, input().split()))[1:]
        lists.append(lst)
    max_sum = -1
    for combination in product(*lists):
        s = sum([x**2 for x in combination])%m
        max_sum = max(max_sum, s)
    print(max_sum)

"""
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
Task

You are given a two lists A and B.
 Your task is to compute their cartesian product AXB.
 Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format

The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.

Both lists have no duplicate integer elements.

Constraints
0 < A < 30
0 < B < 30
"""
from itertools import product
def cartesian_product(A, B):
    return list(product(A, B))
if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(*cartesian_product(A, B))
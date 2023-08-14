"""
Task
Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format
The first line contains an integer N, the number of operations.
The nextN  lines contains the space separated names of methods and their values.

Constraints
0 < N <= 100
"""
from collections import deque
if __name__ == '__main__':
    d = deque()
    for _ in range(int(input())):
        command, *args = input().split()
        getattr(d, command)(*args)
    print(' '.join(map(str, d)))

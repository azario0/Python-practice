"""
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. 
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of  in group A. If it does not appear, print -1.

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions 1  and 3 in group A. 
The second word, 'c', does not appear in group A, so print -1.

Expected output:
1 3
-1
Input Format

The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.

Constraints
1 <= n <= 10000
1 <= m <= 100
1 <= length of each word in the input <= 100
"""
from collections import defaultdict

n,m = map(int,input().split())
A = defaultdict(list)
for i in range(n):
    A[input()].append(i+1)

for i in range(m):
    B = input()
    if B in A:
        print(*A[B])
    else:
        print(-1)
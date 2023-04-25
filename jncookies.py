
"""
esse loves cookies. He wants the sweetness of all his cookies to be greater than value K. To do this, 
Jesse repeatedly mixes two cookies with the least sweetness. He creates a special combined cookie with:

makefile
Copy code
sweetness = (1 * Least sweet cookie + 2 * 2nd least sweet cookie).
He repeats this procedure until all the cookies in his collection have a sweetness >= K. You are given Jesse's cookies. Print the number of operations required to give the cookies a sweetness >= K. Print -1 if this isn't possible.

Input Format
The first line consists of integers N, the number of cookies and K, the minimum required sweetness, separated by a space.
The next line contains N integers describing the array A where A[i] is the sweetness of the i-th cookie in Jesse's collection.

Output Format
Output the number of operations that are needed to increase the cookie sweetness to >= K. Output -1 if this isn't possible.

"""

import heapq
import os

def cookies(k, A):
    heap = A[:]
    heapq.heapify(heap)
    operations = 0
    
    while heap[0] < k and len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + 2*b)
        operations += 1
    
    return operations if heap[0] >= k else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    result = cookies(k, A)
    fptr.write(str(result) + '\n')
    fptr.close()

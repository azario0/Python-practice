"""
There is a horizontal row of  cubes.
The length of each cube is given.
You need to create a new vertical pile of cubes. 
The new pile should follow these directions: if cube[i] is on top of cube[j] then 
sideLength[j] >= sideLength[i].
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example
blocks = [1,2,3,8,7]
Result: No
After choosing the rightmost element, 7, choose the leftmost element, 1. 
After than, the choices are 2 and 8. These are both larger than the top block of size 1.
blocks = [1,2,3,7,8]
Result: Yes

Input Format

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Constraints
1 <= T <= 5
1 <= n <= 10^5
1 <= sideLength < 2^31
"""
def piling_up():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    from collections import deque
    T = int(input())
    for _ in range(T):
        n = int(input())
        d = deque(map(int, input().split()))
        top = 2**31
        while d:
            if d[0] >= d[-1] and d[0] <= top:
                top = d.popleft()
            elif d[-1] >= d[0] and d[-1] <= top:
                top = d.pop()
            else:
                print("No")
                break
        else:
            print("Yes")

if __name__ == '__main__':
    piling_up()
"""
Given an array of integers, find the sum of its elements.

For example, if the array ar=[1,2,3],1+2+4=6 , so return 6.

Function Description

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.

Constraints
0 < n, ar[i] <= 1000
"""
def simpleArraySum(ar):
    total_sum = 0
    for num in ar:
        total_sum += num
    return total_sum

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    print(result)
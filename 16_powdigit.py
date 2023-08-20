"""
2^9 = 512 and the sum of its digits is  5+1+2 =8.

What is the sum of the digits of the number 2^N ?

Input Format

The first line contains an integer T, i.e., number of test cases.
Next T lines will contain an integer .

Constraints
1 <= T <= 100
1 <= N <= 10^4
"""
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    return sum

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_of_digits(2**n))
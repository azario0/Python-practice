"""
Task

You are given a polynomial P of a single indeterminate (or variable),x .
You are also given the values of x and k. Your task is to verify if P(x) = k .

Constraints
All coefficients of polynomial P are integers.
x and y are also integers.

Input Format

The first line contains the space separated values of x and k.
The second line contains the polynomial .

Output Format
Print True if P(x) = k. Otherwise print False
"""

def polynomial_input(x, k):
    return eval(input()) == k
if __name__ == '__main__':
    x, k = map(int, input().split())
    print(polynomial_input(x, k))
"""
Problem: Find the sum of all the primes not greater than a given N.

Input Format: The first line contains an integer T, the number of test cases.
Each of the next T lines contains an integer N.

Constraints:

1 <= T <= 10
1 <= N <= 10^6
"""
def prime_sums(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    prime_sums = [0] * (n + 1)
    for i in range(2, n + 1):
        prime_sums[i] = prime_sums[i-1] + i*primes[i]
    return prime_sums

n = int(input())
prime_sums = prime_sums(10**6)
for _ in range(n):
    m = int(input())
    print(prime_sums[m])

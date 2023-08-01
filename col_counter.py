"""
A counter is a container that stores elements as dictionary keys, 
and their counts are stored as dictionary values.
Task
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.

Constraints
0 < X < 10^3
0 < N <= 10^3
20 < xi < 100
2 < shoe size < 20
"""
from collections import Counter

def main():
    x = int(input())
    shoes = Counter(map(int, input().split()))
    n = int(input())
    income = 0
    for _ in range(n):
        size, price = map(int, input().split())
        if shoes[size]:
            income += price
            shoes[size] -= 1
    print(income)

if __name__ == '__main__':
    main()

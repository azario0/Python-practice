"""
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
 If a new entry overwrites an existing entry, the original insertion position is left unchanged.
 Task

You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each `item_name` and `net_price` in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items,N .
The next N lines contains the item's name and price, separated by a space.

Constraints
0 < N <= 100
"""

def ordered_dict():
    from collections import OrderedDict
    d = OrderedDict()
    for _ in range(int(input())):
        item, space, price = input().rpartition(' ')
        d[item] = d.get(item, 0) + int(price)
    for item, price in d.items():
        print(item, price)

if __name__ == '__main__':
    ordered_dict()
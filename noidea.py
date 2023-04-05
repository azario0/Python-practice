"""
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing integers.
You like all the integers in set A and dislike all the integers in set B. 
Your initial happines is 0. for each i integer in the array i e A, you add 1 to your happiness. if  i e B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.  Note: since A and B are sets, they have not repeated elements. However, the array might contain duplicate elements. Constraints: 1<=n<=10^5, 1<=m<=10^5, 1<= any integer in the input <=10^9
"""
n, m = map(int, input().split())  # Read input values for n and m
arr = list(map(int, input().split()))  # Read input values for array
A = set(map(int, input().split()))  # Read input values for set A
B = set(map(int, input().split()))  # Read input values for set B

happiness = 0  # Initialize happiness to 0
for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)  # Print the final happiness value

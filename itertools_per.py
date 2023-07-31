"""
This tool returns successive  length permutations of elements in an iterable.

If r is not specified or is None, then r defaults to the length of the iterable, 
and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order.
So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
Task

You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string S and the integer value k.

Constraints
0 < k <= len(S)
The string contains only UPPERCASE characters.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

def print_permutations(s: str, k: int) -> None:
    """
    Prints all possible permutations of size k of the string s in lexicographic sorted order.

    Args:
    s (str): The string to permute.
    k (int): The size of the permutations.

    Returns:
    None
    """
    print(*[''.join(i) for i in permutations(sorted(s), k)], sep='\n')

if __name__ == '__main__':
    s, k = input().split()
    print_permutations(s, int(k))

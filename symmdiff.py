"""
Task- Given 2 sets of integers, M and N, print their symmetric difference in ascending order. the term symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""
# read input from stdin
m = int(input())
m_values = set(map(int, input().split()))

n = int(input())
n_values = set(map(int, input().split()))

# compute symmetric difference
result = sorted(list(m_values.symmetric_difference(n_values)))

# print output to stdout
for value in result:
    print(value)


"""
Task- you have a non-empty set s, and you have to execute N cmds given in N lines. The cmds will be pop,remove and discard.  Input format - the first containts integr n, the number of elements in the set s. the second line contains n space separated elements of set s. all of the elements are non-negative integers, <= 9. the third line containts integer N, the number of cmds. the next N lines contains either, pop,remove and/or discard cmds followed by their associated value. Constraints: 0<n<20, 0<N<20 
"""
n = int(input())
s = set(map(int, input().split()))

N = int(input())
for i in range(N):
    cmd = input().split()
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))

print(sum(s))

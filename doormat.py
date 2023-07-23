"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NXM. ( N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Input Format

A single line containing the space separated values of N and M.

Constraints
5 < N < 101
15 < M < 303

"""
def doormat(n,m):
    for i in range(1,n,2):
        print(('.|.'*i).center(m,'-'))
    print('WELCOME'.center(m,'-'))
    for i in range(n-2,-1,-2):
        print(('.|.'*i).center(m,'-'))

if __name__ == '__main__':
    n,m = map(int,input().split())
    doormat(n,m)
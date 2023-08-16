"""
zip([iterable, ...])
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

Average = Sum of scores obtained in all subjects by a student / Total number of subjects
Input Format

The first line contains N and X separated by a space.
The next X lines contains the space separated marks obtained by students in a particular subject.

Constraints
0 < N <= 100
0 < X <= 100
"""

def zipped():
    N, X = map(int, input().split())
    scores = [list(map(float, input().split())) for _ in range(X)]
    for student in zip(*scores):
        print(sum(student)/X)

if __name__ == '__main__':
    zipped()
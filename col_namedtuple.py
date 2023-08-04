"""
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks,class  and name.

Your task is to help Dr. Wesley calculate the average marks of the students.
average = sum of all marks/total students
Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks, IDs,name  and class, under their respective column names.

Constraints
0 < N <= 100
"""
from collections import namedtuple

def main():
    n = int(input())
    columns = input().split()
    Student = namedtuple('Student', columns)
    total = 0
    for _ in range(n):
        student = Student(*input().split())
        total += int(student.MARKS)
    print('{:.2f}'.format(total / n))

if __name__ == '__main__': 
    main()
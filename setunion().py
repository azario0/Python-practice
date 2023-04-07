"""
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets.
Your task is to find the total number of students who have subscribed to at least one newspaper.

Input Format
The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
The second line containsn  space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.
Constrainst:
0< total number of students in college<1000
"""
if __name__ == '__main__':
    n = int(input())
    eng_set = set(map(int, input().split()))
    b = int(input())
    french_set = set(map(int, input().split()))
    
    # Union of sets
    union_set = eng_set.union(french_set)
    
    # Counting the number of students
    num_students = len(union_set)
    
    print(num_students)

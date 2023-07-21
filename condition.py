"""
This Python code defines two lists l and l2 with five and six integers respectively.
 It then checks if any of the numbers in l are negative using an if statement and any() function. 
 If any number is negative, it prints "There are negative numbers in l". 
 Otherwise, it prints "There are no negative numbers in l".
It also checks if all of the numbers in l2 are positive using another if statement and any() function. 
If all numbers are positive, it prints "There are positive numbers in l2".
 Otherwise, it prints "There are no positive numbers in l2".
"""

l = [-1, -2, 0, 1, 2]
l2 = [3, 4, -5, 6, 7, 8]

if any(n < 0 for n in l):
    print("There are negative numbers in l")
else:
    print("There are no negative numbers in l")

if any(n > 0 for n in l2):
    print("There are positive numbers in l2")
else:
    print("There are no positive numbers in l2")
"""
ABC is right triangle, 90 degrees at B.
Therefore, angle ABC = 90 degrees.
Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find  (angle theta, as shown in the figure) in degrees.

Input Format

The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints
0 < AB <= 100
0 < BC <= 100
"""

def angle(theta):
    import math
    return round(math.degrees(math.atan(theta)))

def main():
    AB = int(input('Enter the length of AB : '))
    BC = int(input('Enter the length of BC : '))
    print(angle(AB/BC), chr(176), sep='')

if __name__ == '__main__':
    main()
    
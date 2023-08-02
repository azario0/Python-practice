"""
Task
You are given a complex z. Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number z. 
Note: complex() function can be used in python to convert the input as a complex number.

Constraints

Given number is a valid complex number
"""
def pol_cord(z):
    import cmath
    print(abs(z))
    print(cmath.phase(z))

if __name__ == '__main__':
    z = complex(input())
    pol_cord(z)
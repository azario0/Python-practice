"""
Handling Exceptions
The statements try and except can be used to handle selected exceptions. 
A try statement may have more than one except clause to specify handlers for different exceptions.
Task

You are given two values a and b.
Perform integer division and print a/b.

Input Format

The first line contains T, the number of test cases.
The next  lines each contain the space separated values of a and b.

Constraints
0 < T < 10
"""
def exception_handling():
    for _ in range(int(input())):
        try:
            a,b = map(int, input().split())
            print(a//b)
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as e:
            print("Error Code:",e)
        except Exception as e:
            print("Error Code:",e)
if __name__ == '__main__':
    exception_handling()
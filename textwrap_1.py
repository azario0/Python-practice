"""
You are given a string `S`  and `w` width .
Your task is to wrap the string into a paragraph of width `w` .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns
string: a single string with newline characters ('\n') where the breaks should be
"""
import textwrap

def wrap(string, max_width):
    """
    This function takes a string and a maximum width and returns the string
    wrapped at the specified width using the textwrap module.
    """
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    # Get user input for the string and maximum width
    string = input("Enter a string to wrap: ")
    max_width = input("Enter the maximum width: ")

    # Validate user input
    while not max_width.isdigit():
        max_width = input("Invalid input. Please enter a positive integer for the maximum width: ")
    max_width = int(max_width)

    # Wrap the string and print the result
    result = wrap(string, max_width)
    print(result)
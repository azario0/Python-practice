"""
Problem statement: You are given a text editor with the following four operations:

append - append the given string to the end of the current string.
delete - delete the last k characters of the current string.
print - print the kth character of the current string (1-indexed).
undo - undo the last append or delete operation.
You need to perform q operations on the text editor and print the output of all the print operations.
Constraints:
1 <= q <= 10^6
1 <= k <= |S|, where |S| is the length of the current string.
The sum of the lengths of all strings in the input doesn't exceed 10^6.

Solution:
We can implement the given text editor using a stack. We will maintain a stack of strings, where each string represents the state of the editor after performing a sequence of operations. We will also maintain a stack of integers, where each integer represents the length of the corresponding string on the stack. The top of the stack represents the current state of the editor.
"""
stack = ['']
lengths = [0]
q = int(input())

for i in range(q):
    query = input().split()
    if query[0] == '1':
        s = stack[-1] + query[1]
        stack.append(s)
        lengths.append(lengths[-1] + len(query[1]))
    elif query[0] == '2':
        k = int(query[1])
        s = stack[-1][:-k]
        stack.append(s)
        lengths.append(lengths[-1] - k)
    elif query[0] == '3':
        k = int(query[1])
        print(stack[-1][k-1])
    else:
        stack.pop()
        lengths.pop()

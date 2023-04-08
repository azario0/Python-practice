"""
There are three types of queries that can be performed on a queue:

Enqueue element x into the end of the queue.
Dequeue the element at the front of the queue.
Print the element at the front of the queue.
You are given a sequence of queries of the above types. Your task is to process these queries and output the result.

Function Description:
Complete the twoStacks function in the editor below. It should have the following methods:

push: Enqueue an element to the end of the queue.
pop: Dequeue the element at the front of the queue.
peek: Return the element at the front of the queue.

Constraints:

1 <= q <= 10^5
1 <= type <= 3
1 <= |x| <= 10^9
"""

class MyQueue(object):
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def peek(self):
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack[-1]

    def pop(self):
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack.pop()

    def put(self, value):
        self.first_stack.append(value)

queue = MyQueue()

n = int(input().strip())

for _ in range(n):
    values = input().split()
    if len(values) == 2:
        queue.put(int(values[1]))
    elif values[0] == '2':
        queue.pop()
    else:
        print(queue.peek())

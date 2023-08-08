"""
When users post an update on social media,such as a URL, image, status update etc.,
 other users in their network are able to view this new post on their news feed. 
 Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. 
You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1  and time t2.

Constraints

Input contains only valid timestamps
* year <= 3000
"""
import os, sys

def time_delta(t1, t2):
    """
    t1 and t2 are strings in the format:
    Day dd Mon yyyy hh:mm:ss +xxxx
    """
    from datetime import datetime
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs(t1-t2).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
    
""" if you want to run the code in your local machine, comment out the above lines and uncomment the below lines
```python
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)    
```
    
"""
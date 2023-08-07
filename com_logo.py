"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
They are now trying out various combinations of company names and logos based on this condition.
 Given a string S, which is the company name in lowercase letters, 
 your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

GOOGLE would have it's logo with the letters G,O,E.

Input Format

A single line of input containing the string S.

Constraints
3 < len(S) <= 10^4
S has at least 3 distinct characters
"""

def company_logo(s):
    from collections import Counter
    c = Counter(s)
    most_common = c.most_common()
    third_most_common = most_common[2][1]
    most_common = sorted(filter(lambda x: x[1] >= third_most_common, most_common), key=lambda x: (-x[1], x[0]))
    for i in most_common[:3]:
        print(i[0], i[1])

if __name__ == '__main__':
    s = input()
    company_logo(s)
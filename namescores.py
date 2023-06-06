"""
Given a list of names, 
you need to sort them in alphabetical order and calculate a score for each name based on its alphabetical value. 
The alphabetical value of a name is determined by summing the values of its letters, 
where A has a value of 1, B has a value of 2, and so on.

Once the names are sorted, 
you need to find the position of each query name in the sorted list
and calculate its score by multiplying its alphabetical value with its position in the list.
"""

def calculate_alp_value(name):
    value = 0
    for char in name:
        value += ord(char) - ord('A') +1
    return value
def name_scores(names, queries):
    names.sort()
    scores = {}
    for i, name in enumerate(names,1):
        scores[name] = i * calculate_alp_value(name)
    results = []
    for query in queries:
        results.append(scores[query])
    return results
n = int(input())
names = []
for _ in range(n):
    names.append(input())
    
q = int(input())
queries = []
for _ in range(q):
    queries.append(input())
    
scores = name_scores(names,queries)
for score in scores:
    print(score)



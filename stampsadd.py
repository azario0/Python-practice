"""
Task- Apply your knowledge of .add() operation to help your friend (AI):
AI has a huge collection of country stamples. AI decided to count the total number of distinct country stamps in AI's collection. AI asked for your help. You pick the stamps one by one from a stack of N country stamps. Find the total number of distinct country stamps. Constrainsts- 0<N<1000
"""
n = int(input())
stamps = set()
for i in range(n):
    stamp = input()
    stamps.add(stamp)
print(len(stamps))

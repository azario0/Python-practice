from typing import List

def prob(n: int, s: List[str], k: int) -> float:
    count_a = s.count('a')
    prob_a = count_a / n
    prob_not_a = 1 - prob_a
    prob = 1 - prob_not_a ** k
    return round(prob, 3)

if __name__ == '__main__':
    n = int(input())
    s = input().split()
    k = int(input())
    print(prob(n, s, k))
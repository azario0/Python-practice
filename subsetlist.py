def subsets(list1):
    from itertools import combinations
    subsets = [list(comb) for comb in combinations(list1, 2)]
    return subsets

def final_subsets(list1, size_of_subsets):
    all_subsets = subsets(list1)
    final_subsets = [sub for sub in all_subsets if len(sub) == size_of_subsets]
    final_subsets.reverse()
    return final_subsets

if __name__ == "__main__":
    list1 = list(map(int, input().split()))
    size_of_subsets = int(input())
    print(final_subsets(list1, size_of_subsets))
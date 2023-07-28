from itertools import combinations

def print_subsets(lst):
    subsets = [list(comb) for comb in combinations(lst, 2)]
    #reverse the list
    subsets.reverse()
    print(subsets)

if __name__ == '__main__':
    list1 = input("Enter the list of numbers: ")
    list1 = list(map(int, list1.split()))
    print_subsets(list1)


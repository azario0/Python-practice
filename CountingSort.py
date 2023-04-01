"""
Quicksort usually has  a runninng time of n x log(n), but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e, they sort a list just  by comparing the elements to one another. A comparison sort algorithm cannot beat n x log(n) (worst case) running time, since n x log(n) represents the minimum number of comparisons needed to know where to place each element. 
Alternating sorting - the counting sort does not require comparison. instead, you create an integer array whose index range covers the entire range of values in your array to sort. each time a value occurs in the original array, you increment the counter at that index. at the end, run through your counting array, printing the value of each non-zero valued index that the number of times. def countingSort(arr):
"""
def countingSort(arr):
    n = len(arr)
    result = [0] * 100
    
    for i in range(n):
        result[arr[i]] += 1
    return result
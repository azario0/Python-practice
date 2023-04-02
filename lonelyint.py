""" 
Given an arr of integers, where all elements but one occur twice, find the unique element.
"""
def lonelyinteger(arr):
    unique = 0
    for i in arr:
        unique ^= i
    return unique
"""
* Initialize a variable `unique to 0
* iteratre through each number in the input arr `arr` and the current number `i`. This operation has the property of being both commutatitve and associative, which means that it can be used to find the unique element in the arr. Specifically, if a number appears twice in arr. its XOR value will be 0, so it will cancel out. The final result will be the XOR of all the numbers that appear  only once in the arr.
* We return the final value of `unique`, which represents unique element in the array.
"""
arr = list(map(int, input().rstrip().split()))
print(lonelyinteger(arr))
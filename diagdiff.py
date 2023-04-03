""" Given a square matrix, calculate the absolute difference between the sums of its diagonals"""

def diagonaldiff(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0
    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - i - 1]
    return abs(primary_sum - secondary_sum)

"""
* first find the size of the square matrix by taking length of the array `arr`. Since `arr` is square matrix, its length represents number of rows and columns.
* We initilize two variables `primary_sum` and `secondary_sum` to  0.
* These variables will store the sums of diagnonals of the matrix respectively.
* use loop to iterate through each row of the matrix. for each row, we add the element at the corresponding position on the primary diagonal to `primary_sum`, and the element at corresponding position on the secong diagonal to ` secondary_sum`.
* calculate the abs diff between `primary_sum` and `secondary_sum`, and return the result
"""

arr = [[1,2,3], [4,5,6], [7,8,9]]
print(diagonaldiff(arr))
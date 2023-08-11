"""
To solve this task, you can use dynamic programming to calculate the number of paths for each point on the grid.
You can start by initializing a 2D array with all values set to 1. 
Then, iterate through the array and update each value by adding the value above and to the left of it. 
Finally, return the value at the bottom right corner of the array.
"""
def lattice_paths(n, m):
    # Initialize a 2D array with all values of 1's
    paths = [[1] * (m+1) for _ in range(n+1)]
    #update each value using dynamic programming
    for i in range(1, n+1):
        for j in range(1, m+1):
            paths[i][j] = paths[i-1][j] + paths[i][j-1]
            #return the value at the bottom right corner of the array
    return paths[n][m] % (10**9 + 7)

# Get input from user
t = int(input("Enter the number of test cases: "))
for i in range(t):
    m, n = map(int, input("Enter the dimensions of the grid: ").split())
    print(lattice_paths(m, n))

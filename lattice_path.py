"""
To solve this task, you can use dynamic programming to calculate the number of paths for each point on the grid.
You can start by initializing a 2D array with all values set to 1. 
Then, iterate through the array and update each value by adding the value above and to the left of it. 
Finally, return the value at the bottom right corner of the array.
"""
def lattice_paths(n):
    # Initialize a 2D array of 1's
    paths = [[1 for _ in range(n + 1)] for _ in range(n + 1)]

    # Calculate the number of paths for each point on the grid
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

    # Return the value at the bottom right corner of the array
    return paths[n][n]
if __name__ == "__main__":
    print(lattice_paths(int(input("Enter the number: "))))
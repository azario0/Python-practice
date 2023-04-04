"""
Given a square grid of characters in the arrage ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom.
Return YES if they are or NO if they are not.  
Function description: gridChallenge has the following params 
string grind[n]: an arra of strings . 
Returns string : either YES or NO. 
constraints 
1<= t <=100, 
1<=n<=100. Each string consists of lowercase letters in the range ascii[a-z]
"""
def gridChallenge(grid):
    n = len(grid)
    m = len(grid[0])
    
    # sort each row
    for i in range(n):
        grid[i] = sorted(grid[i])
    
    # check columns
    for j in range(m):
        for i in range(n-1):
            if grid[i][j] > grid[i+1][j]:
                return "NO"
    
    return "YES"

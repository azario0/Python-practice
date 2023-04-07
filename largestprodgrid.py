"Diagonal problem, finding the largest product in grid"

def largest_product_in_grid(grid, size):
    max_product = 0
    for i in range(size):
        for j in range(size):
            if i < size - 3:
                # Check vertical products
                product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
                if product > max_product:
                    max_product = product
            if j < size - 3:
                # Check horizontal products
                product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
                if product > max_product:
                    max_product = product
                # Check diagonal products (top-left to bottom-right)
                if i < size - 3:
                    product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
                    if product > max_product:
                        max_product = product
                # Check diagonal products (bottom-left to top-right)
                if i >= 3:
                    product = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
                    if product > max_product:
                        max_product = product
    return max_product

if __name__ == '__main__':
    grid = []
    for _ in range(20):
        row = list(map(int, input().split()))
        grid.append(row)
    print(largest_product_in_grid(grid, 20))

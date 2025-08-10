def flip_submatrix_vertically(grid, x, y, k):
    for i in range(k // 2):
        row1 = x + i
        row2 = x + (k - 1 - i)
        for col in range(y, y + k):
            grid[row1][col], grid[row2][col] = grid[row2][col], grid[row1][col]
    return grid

# Example 1
grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(flip_submatrix_vertically(grid, 1, 0, 3))
# Output: [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]

# Example 2
grid = [[3,4,2,3],[2,3,4,2]]
print(flip_submatrix_vertically(grid, 0, 2, 2))
# Output: [[3,4,4,2],[2,3,2,3]]
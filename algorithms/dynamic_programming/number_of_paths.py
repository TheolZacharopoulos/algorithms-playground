paths = [[1, 1, 1],
         [1, 1, 1],
         [1, 0, 1]
         ]


def find_paths_rec(grid, row=0, col=0):
    if grid[row][col] == 0:
        return 0

    # the end
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return 1

    left = 0
    down = 0
    if row != len(grid) - 1:
        left = find_paths_rec(grid, row + 1, col)

    if col != len(grid) - 1:
        down = find_paths_rec(grid, row, col + 1)

    return left + down


def find_paths_mem(grid, row, col, p):
    if grid[row][col] == 0:
        return 0

    # the end
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return 1

    if p[row][col] != -1:
        return p[row][col]

    left = 0
    down = 0
    if row != len(grid) - 1:
        left = find_paths_rec(grid, row + 1, col)

    if col != len(grid) - 1:
        down = find_paths_rec(grid, row, col + 1)

    p[row + 1][col] = left
    p[row][col + 1] = down

    return left + down


def find_paths_dp(grid):
    rows = len(grid)
    cols = len(grid[0])

    sub = [[0 for _ in range(cols)] for _ in range(rows)]

    sub[rows - 1][cols - 1] = 1

    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if i == rows - 1 and j == cols - 1:
                sub[i][j] = 1

            elif i == rows - 1:
                sub[i][j] = sub[i][j + 1]

            elif j == cols - 1:
                sub[i][j] = sub[i + 1][j]

            else:
                sub[i][j] = sub[i + 1][j] + sub[i][j + 1]

            if grid[i][j] == 0:
                sub[i][j] = 0

    return sub[0][0]

print(find_paths_rec(paths))
print(find_paths_mem(paths, 0, 0, [[-1 for _ in range(len(paths[0]))] for _ in range(len(paths))]))
print(find_paths_dp(paths))

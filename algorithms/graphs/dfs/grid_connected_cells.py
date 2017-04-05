# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid


def get_biggest_region(grid):
    max_region = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_region = max(max_region, count_region(grid, i, j))

    return max_region


def count_region(grid, i, j):
    # region out of range
    if not (i in range(len(grid)) and (j in range(len(grid[0])))):
        return 0

    # ignore 0 regions
    if grid[i][j] == 0:
        return 0

    # set grid place
    grid[i][j] = 0

    count = 1

    count += count_region(grid, i - 1, j - 1)
    count += count_region(grid, i - 1, j)
    count += count_region(grid, i - 1, j + 1)
    count += count_region(grid, i, j - 1)
    count += count_region(grid, i, j + 1)
    count += count_region(grid, i + 1, j - 1)
    count += count_region(grid, i + 1, j)
    count += count_region(grid, i + 1, j + 1)

    return count

n = int(input().strip())
m = int(input().strip())

grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)

print(get_biggest_region(grid))

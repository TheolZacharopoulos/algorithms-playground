"""
Imagine a robot sitting on the upper left hand corner of an NxN grid.
The robot can only move in two directions: right and down.
How many possible paths are there for the robot?

FOLLOW UP:
Imagine certain squares are “off limits”, such that the robot can not step on them.
Design an algorithm to get all possible paths for the robot.
"""


def count_paths(grid, row, col):
    if not is_valid(grid, row, col):
        return 0

    if is_at_the_end(grid, row, col):
        return 1

    return count_paths(grid, row + 1, col) + count_paths(grid, row, col + 1)


def count_paths_memo(grid, row, col, paths=None):
    if paths is None:
        paths = [[0] * len(grid)] * len(grid[row])

    if not is_valid(grid, row, col):
        return 0

    if is_at_the_end(grid, row, col):
        return 1

    if paths[row][col] == 0:
        paths[row][col] = count_paths(grid, row + 1, col) + count_paths(grid, row, col + 1)

    return paths[row][col]


def count_paths_dyn_prog(grid, row, col):
    paths = [[0] * len(grid)] * len(grid[row])

    for i in range(len(grid)):
        paths[i][0] = 1

    for j in range(len(grid[row])):
        paths[0][j] = 1

    for i in range(len(grid)-2, -1, -1):
        for j in range(len(grid[row])-2, -1, -1):

            if is_valid(grid, i + 1, j) and is_valid(grid, i, j + 1):
                paths[i][j] = paths[i + 1][j] + paths[i][j + 1]

            elif is_valid(grid, i + 1, j):
                paths[i][j] = paths[i + 1][j]

            elif is_valid(grid, i, j + 1):
                paths[i][j] = paths[i][j + 1]

    return paths[0][0]


def is_valid(grid, row, col):
    if row > len(grid)-1 or col > len(grid[row])-1 or grid[row][col] == -1:
        return False
    return True


def is_at_the_end(grid, row, col):
    return row == len(grid)-1 and col == len(grid[row])-1

if __name__ == '__main__':
    g1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    g2 = [
        [0, 0, 0],
        [0, -1, 0],
        [0, 0, 0]
    ]

    print(count_paths(g1, 0, 0))
    print(count_paths(g2, 0, 0))

    print(count_paths_memo(g1, 0, 0))
    print(count_paths_memo(g2, 0, 0))

    print(count_paths_dyn_prog(g1, 0, 0))
    print(count_paths_dyn_prog(g2, 0, 0))

# https://www.hackerrank.com/challenges/2d-array

# Given a  2D Array, :
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
#
# We define an hourglass in  to be a subset of values with indices
# falling in this pattern in 's graphical representation:
# a b c
#   d
# e f g
#
# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
#
# Task:
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]
       ]


def sum_hourglass(array):
    rows = len(array)
    cols = len(array[0])

    sums = [0 for _ in range(16)]
    max_sum = float('-inf')
    k = 0

    # just go in between (not start or end)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            top = array[i - 1][j - 1] + array[i - 1][j] + array[i - 1][j + 1]
            mid = array[i][j]
            bot = array[i + 1][j - 1] + array[i + 1][j] + array[i + 1][j + 1]
            sums[k] = top + mid + bot
            k += 1

    for s in range(k):
        max_sum = max(max_sum, sums[s])

    return max_sum

print(sum_hourglass(arr))

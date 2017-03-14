# Objective: Given two dimensional matrix,
# write an algorithm to find out the snake sequence which has the max­i­mum length.
# There could be many snake sequence in the matrix,
# you need to return the one with the max­i­mum length.
# Travel is allowed only in two directions, either go right OR go down.

# What is snake sequence: Snake sequence can be made if num­ber in adjacent
# right cell or num­ber in the adjacent down cell is either +1 or –1 from the num­ber in the current cell.

arr = [[1, 2, 1, 2],
       [7, 7, 2, 5],
       [6, 4, 3, 4],
       [1, 2, 2, 5]
       ]


def find_snake(array):
    rows = len(array)
    cols = len(array[0])
    maxLen = 1

    # every cell is a sequence of len 1
    result = [[1 for _ in range(cols)] for _ in range(rows)]

    for i in range(0, rows):
        for j in range(0, cols):
            # check from left
            if i > 0 and abs(array[i][j] - array[i - 1][j]) == 1:
                result[i][j] = max(result[i][j], result[i - 1][j] + 1)
                maxLen = max(maxLen, result[i][j])

            # check from top
            if j > 0 and abs(array[i][j] - array[i][j - 1]) == 1:
                result[i][j] = max(result[i][j], result[i][j - 1] + 1)
                maxLen = max(maxLen, result[i][j])

    return maxLen


print(find_snake(arr))

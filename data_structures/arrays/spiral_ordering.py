"""
A 2D array can be written as a sequence in several orders the most natural ones
being row-by-row or column-by-column. In this problem we explore the problem of
writing the 2D array in spiral order.
For example, the spiral ordering for an 2D array

(1, 2, 3,
 4, 5, 6,
 7, 8, 9)

 is (1,2,3, 6,9,8, 7,4,5).

Here is a uniform way of adding the boundary:
Add the first n - 1 elements of the first row.
Then add the first n-1 elements of the last column.
Then add the last n-1 elements of the last row in reverse order.
Finally, add the last n-1 elements of the first column in reverse order.

The time complexity is 0(n2) and the space complexity is 0(1).
"""
import math


def spiral(array):
    spiral_ordering = []
    for offset in range(int(math.ceil(0.5 * len(array)))):
        layer_clockwise(array, offset, spiral_ordering)
    return spiral_ordering


def layer_clockwise(matrix, offset, spiral_ordering):
    # The end: matrix has odd dimension, and we are at its center.
    if offset == len(matrix) - offset - 1:
        spiral_ordering.append(matrix[offset][offset])
        return

    for j in range(len(matrix) - offset - 1):
        spiral_ordering.append(matrix[offset][j])

    for i in range(len(matrix) - offset - 1):
        spiral_ordering.append(matrix[i][len(matrix) - offset - 1])

    for j in range(len(matrix) - offset - 1, offset, -1):
        spiral_ordering.append(matrix[len(matrix) - offset - 1][j])

    for i in range(len(matrix) - offset - 1, offset, -1):
        spiral_ordering.append(matrix[i][offset])

if __name__ == '__main__':
    print(spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

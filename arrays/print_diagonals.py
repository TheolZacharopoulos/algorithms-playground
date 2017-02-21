# http://algorithms.tutorialhorizon.com/print-all-diagonals-of-a-given-matrix/
# Given two dimensional matrix, write an algorithm to print all the diagonals of matrix.

a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]
     ]


def print_diagonals(array):
    # First half
    row = 0
    while row < len(array):
        col = 0
        temp_row = row
        while temp_row >= 0:
            print(str(array[temp_row][col]) + ' ', end='')
            temp_row -= 1
            col += 1
        print("")
        row += 1

    # Second half
    # col 0 is already done previously
    col = 1
    while col < len(array):
        row = len(array)-1
        temp_col = col
        while temp_col <= len(array)-1:
            print(str(array[row][temp_col]) + ' ', end='')
            row -= 1
            temp_col += 1
        print("")
        col += 1


print_diagonals(a)

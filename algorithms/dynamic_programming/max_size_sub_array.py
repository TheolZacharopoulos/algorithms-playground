# Given a matrix of 0’s and 1’s (binary matrix). Find out Maximum size square sub-matrix with all 1’s.

arr = [[0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0],
       [0, 1, 1, 1, 1, 0],
       [0, 0, 1, 1, 1, 0],
       [1, 1, 1, 1, 1, 1]
       ]

arr1 = [[0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1]
        ]


def find_sum(array):
    rows = len(array)
    cols = len(array[0])

    temp = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(0, rows):
        temp[i][0] = array[i][0]

    for j in range(0, cols):
        temp[0][j] = array[0][j]

    theMax = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if array[i][j] == 1:
                temp[i][j] = min(temp[i - 1][j], temp[i][j - 1], temp[i - 1][j - 1]) + 1
            else:
                temp[i][j] = 0
            theMax = max(theMax, temp[i][j])

    return theMax


print(find_sum(arr))
print(find_sum(arr1))

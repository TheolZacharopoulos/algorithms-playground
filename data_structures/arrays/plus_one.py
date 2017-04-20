"""
Write a program which takes as input an array of digits encoding a decimal number D
and updates the array to represent the number D + 1.
For example, if the input is (1,2,9) then you should update the array to (1,3,0).
Another example: if the input is (9,9,9) then you should update the array to (1,0,0,0).

Brute force: Convert input array to integer, add one, put elements back to an array.
This solution can overflow for huge numbers.
We need to operate in the arrays, use the algorithm from school (with the carries).
"""


def plus_one(input):
    # work from the least significant digits (reversed order)
    input[-1] += 1

    for i in range(len(input) - 1, 0, -1):
        if input[i] == 10:
            input[i] = 0
            input[i - 1] += 1  # carry

    # Needs additional digit as the most significant digit
    # has a carry-out .
    if input[0] == 10:
        input[0] = 0
        input.insert(0, 1)


if __name__ == '__main__':
    i_1 = [1, 2, 9]
    plus_one(i_1)
    print(i_1)

    i_2 = [9, 9, 9]
    plus_one(i_2)
    print(i_2)

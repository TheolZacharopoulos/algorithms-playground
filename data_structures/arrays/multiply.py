"""
Certain applications require arbitrary precision arithmetic.
One way to achieve this is to use arrays to represent integers, e.g., with one digit per array entry,
with the most significant digit appearing first, and a negative leading digit denoting a negative integer.
For example, (1,9,3,7,0,7,7,2,1) represents 193707721 and (-7,6,1,8,3,8,2,5,7,2,8,7) represents -761838257287.

Write a program that takes two arrays representing integers,
and returns an integer representing their product.
For example, since 193707721 X -761838257287 = -147573952589676412927,
if the inputs are (1,9,3,7,0,7,7,2,1) and (-7,6,1,8,3,8,2,5,7,2,8,7),
your function should return (-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7).

Brute force: Convert input array to integer, add one, put elements back to an array.
This solution can overflow for huge numbers.

We can use the grade-school algorithm for multiplication which consists of
multiplying the first number by each digit of the second,
and then adding all the resulting terms.
From a space perspective, it is better to incrementally add the terms rather
than compute all of them individually and then add them up.
The number of digits required for the product is at most n + m
for n and m digit operands, so we use an array of size n + m for the result.

For example, when multiplying 123 with 987,
we would form 7 X 123 = 861, then we would form 8 X 123 X 10 = 9840,
which we would add to 861 to get 10701.
Then we would form 9 X 123 X 100 = 110700,
which we would add to 10701 to get the final result 121401.
(All numbers shown are represented using arrays of digits.)
  123
x 987 =
7 * 123 = 861
8 * 123 * 10 = 9840 (861 + 9840 = 10701)
9 * 123 * 100 = 110700 (10701 + 110700 = 121401)

There are m partial products, each with at most n + 1 digits.
We perform 0(1) operations on each digit in each partial product,
so the time complexity is 0(nm).
"""

def muliply(num_1, num_2):
    # extract sign and then ignore it at the beggining
    sign =  1
    if num_1[0] < 0 or num_2[0] < 0:
        sign = -1
    num_1[0] = abs(num_1[0])
    num_2[0] = abs(num_2[0])

    result = [0] * (len(num_1) + len(num_2))

    for i in range(len(num_1)-1, -1, -1):
        for j in range(len(num_2)-1, -1, -1):
            result[i + j + 1] = result[i + j + 1] + (num_1[i] * num_2[j])
            result[i + j] = result[i + j] + result[i + j + 1] / 10
            result[i + j + 1] = result[i + j + 1] % 10

    # Removing the leading zeros
    first_not_zero = 0
    while first_not_zero < len(result) and result[first_not_zero] == 0:
        first_not_zero += 1

    result = result[first_not_zero:len(result)]

    if not result:
        return [0]

    # add the sign
    result[0] *= sign

    return result

if __name__ == '__main__':
    i_1 = [1,9,3,7,0,7,7,2,1]
    i_2 = [-7,6,1,8,3,8,2,5,7,2,8,7]
    print(muliply(i_1, i_2))

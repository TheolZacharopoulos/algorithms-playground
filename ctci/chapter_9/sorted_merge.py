"""
You are given two sorted arrays, A and B, and A has a large enough buffer at the end to hold B.
Write a method to merge B into A in sorted order.
"""


def merge(array_a, array_b, last_a):
    last_b = len(array_b)

    index_a = last_a - 1  # Index of last element in array a
    index_b = last_b - 1  # Index of last element in array b
    index_merged = last_a + last_b - 1

    # Merge a and b, starting from the last element in each
    while index_b >= 0:
        # end of a is > than end of b
        if index_a >= 0 and array_a[index_a] > array_b[index_b]:
            array_a[index_merged] = array_a[index_a]
            index_a -= 1
        else:
            array_a[index_merged] = array_b[index_b]
            index_b -= 1
        index_merged -= 1


if __name__ == '__main__':
    arrayA = [1, 3, 5, 7, 9, 0, 0, 0, 0, 0]
    arrayB = [2, 4, 6, 8, 10]

    merge(arrayA, arrayB, 5)

    print(arrayA)
    print(arrayB)

# Objective: Given a sorted array of distinct integers, Find the Magic index or Fixed point in the array.
# Magic Index or Fixed Point: Magic index or a Fixed point in an array is an index i in the array such that A[i] = i.

a = [-1, 0, 1, 2, 4, 10]


# Easy if use binary search
def find_magic_index(array, start, end):
    n = len(array)

    # Not found
    if n == 0:
        return -1

    mid = int((start + end) / 2)

    # magic index:
    if array[mid] == mid:
        return mid

    if array[mid] > mid:
        return find_magic_index(array, 0, mid)
    else:
        return find_magic_index(array, mid + 1, n)


print(find_magic_index(a, 0, len(a)))

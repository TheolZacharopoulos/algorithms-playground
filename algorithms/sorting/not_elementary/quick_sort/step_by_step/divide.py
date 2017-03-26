# https://www.hackerrank.com/challenges/quicksort1

# Choose some pivot element , p, and partition your unsorted array, arr,
# into three smaller arrays: left, right, and equal, where each element in left < p,
# each element in right > p, and each element in equal = p.

# Given arr and p=arr[0], partition arr into left, right, and equal using the Divide instructions above.
# Then print each element in left followed by each element in right, followed by each element in equal on a single line.
# Your output should be space-separated.


def divide_extraspace(array):
    left = []
    right = []
    equal = []

    p = array[0]

    for i in range(len(array)):
        if array[i] < p:
            left.append(array[i])
        elif array[i] > p:
            right.append(array[i])
        else:
            equal.append(array[i])

    return left + equal + right


def divide_inplace(array):
    """
    Partition Details:
     1. While i and j are not crossed:
        - Scan i from left to right while a[i] < a[low]
        - Scan j from right to left while a[j] > a[low]
        - Swap a[i] and a[j]
     2. When pointers crossed
        - Swap a[low] and a[j]
     """
    if len(array) == 1:
        return array

    low = 0
    left = low + 1

    hi = len(array) - 1
    right = hi

    while left < right:
        while left <= right and array[left] < array[low]:
            left += 1

        while left <= right and array[right] > array[low]:
            right -= 1

        # scans did not strictly cross
        if left <= right:
            # swap
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    # pointers crossed, swap
    array[low], array[right] = array[right], array[low]

    return array

print(' '.join(map(str, ([4, 5, 3, 7, 2]))))
print(' '.join(map(str, divide_extraspace([4, 5, 3, 7, 2]))))
print(' '.join(map(str, divide_inplace([4, 5, 3, 7, 2]))))


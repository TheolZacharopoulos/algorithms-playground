# 1. Insertion sort improvement:
#  - Merge sort is too much overhead for tiny sub-arrays
#  - Cutoff to Insertion sort for ~7 items
#  - Maybe even 20% faster

# 2. Stop if it already sorted:
#  - is biggest item int first half <= smallest item in the second half?
#  - helps a lot for partially ordered arrays
#  - Almost linear time

from algorithms.sorting.elementary.insertion_sort import insertion_sort
from algorithms.sorting.not_elementary.merge_sort.merge_sort import merge

CUTOFF = 7


def merge_sort(array):
    n = len(array)

    if n == CUTOFF:
        return insertion_sort(array)

    if n < 2:
        return array

    # divide
    mid = n // 2
    array_low = array[0: mid]
    array_high = array[mid: n]

    # conquer (with recursion)
    merge_sort(array_low)
    merge_sort(array_high)

    # IMPROVEMENT 2 (Already sorted):
    # if array[mid-1] < array[mid]:
    #     return array

    # merge results
    return merge(array_low, array_high, array)


if __name__ == "__main__":
    print(merge_sort([5, 4, 2, 1, 3, 11, 14, 27, 35, 35, 25, 6, 34, 23, 6, 88, 345]))
    print(merge_sort([5, 4, 2, 1, 3]))
    print(merge_sort([8, 5, 3, 4, 9, 7, 12, 13, 14]))
    print(merge_sort([1, 2, 3, 4, 5, 6]))

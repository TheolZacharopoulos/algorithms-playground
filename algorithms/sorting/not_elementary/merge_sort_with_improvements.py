# 1. Insertion sort improvement:
#  - Merge sort is too much overhead for tiny sub-arrays
#  - Cutoff to Insertion sort for ~7 items
#  - Maybe even 20% faster

# 2. Stop if it already sorted:
#  - is biggest item int first half <= smallest item in the second half?
#  - helps a lot for partially ordered arrays
#  - Almost linear time

from algorithms.sorting.elementary.insertion_sort import insertion_sort
from algorithms.sorting.not_elementary.merge_sort import merge

CUTOFF = 7


def sort(array, aux, low, high):
    # IMPROVEMENT 1
    if high <= low + CUTOFF - 1:
        return insertion_sort(array)

    # check if end
    if high <= low:
        return array

    # find the mid point
    mid = int(low + (high - low) / 2)

    # sort the left half
    sort(array, aux, low, mid)

    # sort the right half
    sort(array, aux, mid + 1, high)

    # IMPROVEMENT 2:
    if not array[mid + 1] < array[mid]:
        return array

    # merge them together
    merge(array, aux, low, mid, high)

    return array


def merge_sort(array):
    aux = [0] * len(array)
    return sort(array, aux, 0, len(array) - 1)


if __name__ == "__main__":
    print(merge_sort([5, 4, 2, 1, 3, 11, 14, 27, 35, 35, 25, 6, 34, 23, 6, 88, 345]))
    print(merge_sort([5, 4, 2, 1, 3]))
    print(merge_sort([8, 5, 3, 4, 9, 7, 12, 13, 14]))

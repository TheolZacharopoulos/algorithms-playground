# Basic plan:
# 1. Shuffle the array (for better performance)
# 2. Partition the array for some j:
#  - entry a[j] is in place
#  - No larger entry to the left of j
#  - No smaller entry to the right of j
# 3. Sort each piece recursively

# Partition Details:
# 1. While i and j are not crossed:
#    - Scan i from left to right while a[i] < a[low]
#    - Scan j from right to left while a[j] > a[low]
#    - Swap a[i] and a[j]
# 2. When pointers crossed
#    - Swap a[low] and a[j]

from random import shuffle


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(array, lo, hi):
    left = lo + 1

    right = hi

    while True:
        while left <= right and array[left] < array[lo]:
            left += 1

        while left <= right and array[right] > array[lo]:
            right -= 1

        # scans did not strictly cross
        if left <= right:
            swap(array, left, right)
            left += 1
            right -= 1

        # pointers crossed
        if left >= right:
            swap(array, lo, right)
            break

    return right


def _quick_sort(arr, lo, hi):
    if lo > hi:
        return

    j = partition(arr, lo, hi)
    _quick_sort(arr, lo, j - 1)
    _quick_sort(arr, j + 1, hi)


def quick_sort(array):
    shuffle(array)
    _quick_sort(array, 0, len(array) - 1)


if __name__ == "__main__":
    arr = [5, 4, 1, 2, 7, 6, 8, 9, 10, 3]
    print(arr)
    quick_sort(arr)
    print(arr)

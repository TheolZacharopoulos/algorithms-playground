# Basic plan:
# 1. Shuffle the array (for better performance)
# 2. Partition the array for some j:
#  - entry a[j] is in place
#  - No larger entry to the left of j
#  - No smaller entry to the right of j
# 3. Sort each piece recursively    

from random import shuffle


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(a, lo, hi):
    i = lo + 1
    j = hi

    while True:
        while a[i] < a[lo]:
            if i == hi:
                break
            i += 1

        while a[lo] < a[j]:
            if j == lo:
                break
            j -= 1

        if i >= j:
            break
        swap(a, i, j)
    swap(a, lo, j)
    return j


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
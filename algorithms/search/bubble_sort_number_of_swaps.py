# https://www.hackerrank.com/challenges/ctci-bubble-sort


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(array):
    is_sorted = False
    last_unsorted = len(array) - 1
    num_of_swaps = 0

    while not is_sorted:
        is_sorted = True

        for i in range(last_unsorted):
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                is_sorted = False
                num_of_swaps += 1

        last_unsorted -= 1

    print("Array is sorted in " + str(num_of_swaps) + " swaps.")
    print("First Element: " + str(array[0]))
    print("Last Element: " + str(array[-1]))


bubble_sort([1, 2, 3])
bubble_sort([3, 2, 1])

# In the i'th iteration find the smallest remaining entry to the bigger index of i and swap that with i.
# after each swap the left of the i is always in order.
#
# while i less than the array's length:
#     find the smallest
#     swap with i
#     increment i
#
# Invariants:
# - Entries to the left never change
# - No entry to the right is smaller than any element on the left
#
# [1/2 * N^2] -> O(N^2) time (even if the input is sorted)
# Linear time of exchanges, every item is put into its final position with just 1 exchange
#
# NOT Stable


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(array):
    for i in range(len(array)):
        min_pos = i

        for j in range(i+1, len(array)):

            # find the smaller
            if array[j] < array[min_pos]:
                min_pos = j

        # swap i with the smallest
        swap(array, i, min_pos)

    return array


def selection_sort_recursive_wrap(array):
    return selection_sort_recursive(array, 0)


def selection_sort_recursive(array, start):
    if start < len(array)-1:
        min_pos = start

        # find min
        for j in range(start, len(array)):
            if array[j] < array[min_pos]:
                min_pos = j

        # swap
        swap(array, start, min_pos)

        # recursive (tail recursion)
        return selection_sort_recursive(array, start + 1)
    else:
        return array

if __name__ == "__main__":
    print(selection_sort([5, 4, 2, 1, 3]))
    print(selection_sort_recursive_wrap([5, 4, 2, 1, 3]))

# Move entries more than one positions at a time, by h-sorting the array.
# An h-sorted array is h interleaved sorted subsequences
# We start with pos 1 and we look at every h'th element
# then start at pos 2 and do the same
# we h-sort the array for decreasing sequence of values of h
#
# How we h-sort? : Insertion sort but when we go backwards on the array, we skip by h instead by 1.
# Slightly more complicated code than insertion sort but much more efficient (unless huge arrays)
# it is used in embedded system because it is small
# for 3h+1 sequence worst case is: O(n^3/2) but normally a lot less


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def shell_sort(array):
    h = 1

    # compute the increments based on the array's length
    while h < (len(array) / 3):
        # 1, 4, 13, 40, 121, ...
        h = 3 * h + 1

    while h >= 1:
        # h-sort the array
        for i in range(int(h), len(array)):
            for j in range(i, int(h)-1, -int(h)):
                if array[j] < array[j - int(h)]:
                    swap(array, j, j - int(h))
        h /= 3

    return array


if __name__ == "__name__":
    print(shell_sort([5, 4, 2, 1, 3]))

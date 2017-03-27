# until the array is ordered <- O(N) time
#     walk through           <- O(N) time
#     swap out of order elements
#
# So O(N^2) time and O(1) space


def bubble_sort(array):
    is_sorted = False
    last_unsorted = len(array) - 1

    while not is_sorted:
        # Assume it is sorted
        is_sorted = True

        for i in range(last_unsorted):
            if array[i] > array[i + 1]:

                # swap the two values
                array[i], array[i + 1] = array[i + 1], array[i]

                # hey it is not sorted yet
                is_sorted = False

        # shrink the array since the last item is now sorted
        last_unsorted -= 1
    return array

if __name__ == "__main__":
    print(bubble_sort([5, 4, 2, 1, 3]))

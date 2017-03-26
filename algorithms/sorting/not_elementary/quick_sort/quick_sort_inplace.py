# Optimization:
# quick sort without creating containers on each recursive call.


def inplace_quick_sort(array, low, high):
    """Sort the list from S[low] to S[high] inclusive using the quick-sort algorithm."""
    if low >= high:
        return  # range is trivially sorted

    pivot = array[high]  # last element of range is pivot
    left = low  # will scan rightward
    right = high - 1  # will scan leftward

    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and array[left] < pivot:
            left += 1

        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < array[right]:
            right -= 1

        if left <= right:  # scans did not strictly cross
            array[left], array[right] = array[right], array[left]  # swap values
            left, right = left + 1, right - 1  # shrink range

    # put pivot into its final place (currently marked by left index)
    array[left], array[high] = array[high], array[left]

    # make recursive calls
    inplace_quick_sort(array, low, left - 1)
    inplace_quick_sort(array, left + 1, high)


if __name__ == "__main__":
    arr = [1, 3, 9, 8, 2, 7, 5]
    print(arr)
    inplace_quick_sort(arr, 0, len(arr) - 1)
    print(arr)

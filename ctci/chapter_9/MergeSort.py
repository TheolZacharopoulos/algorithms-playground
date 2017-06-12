def merge(arr, left_start, right_end):
    mid = (right_end + left_start) // 2
    left_end = mid
    right_start = left_end + 1

    array_size = right_end - left_start + 1

    tmp_arr = [0] * array_size

    left = left_start
    right = right_start

    index = left_start

    # walk through the arrays and always copy the smaller element
    while left <= left_end and right <= right_end:
        if arr[left] <= arr[right]:
            tmp_arr[index] = arr[left]
            left += 1
        else:
            tmp_arr[index] = arr[right]
            right += 1
        index += 1

    # copy the remainder elements
    remainder = mid - left

    for i in range(0, remainder):
        arr[index + i] = tmp_arr[left + i]


def merge_sort(arr, left_start, right_end):
    # base case
    if left_start >= right_end:
        return

    mid = (left_start + right_end) // 2

    merge_sort(arr, left_start, mid)
    merge_sort(arr, mid + 1, right_end)

    merge(array, left_start, right_end)


if __name__ == '__main__':
    array = [1, 2, 3, 1, 5, 8, 4, 2]
    merge_sort(array, 0, len(array))
    print(array)

def bubble_sort(arr):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False


def bubble_sort_opt1(arr):
    """
    The last element will be in place after each pass
    """
    is_sorted = False
    last_unsorted = len(arr) - 1

    while not is_sorted:
        is_sorted = True
        for i in range(0, last_unsorted):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        last_unsorted -= 1


if __name__ == '__main__':
    array1 = [1, 3, 5, 1, 2, 9, 5, 6]
    bubble_sort(array1)
    print(array1)

    array2 = [1, 3, 5, 1, 2, 9, 5, 6]
    bubble_sort_opt1(array2)
    print(array2)

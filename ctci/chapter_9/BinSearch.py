def bin_search_rec(arr, elem, start, end):
    if start >= end:
        return False

    mid = (start + end) // 2

    if arr[mid] == elem:
        return True
    elif elem > arr[mid]:
        return bin_search_rec(arr, elem, mid + 1, end)
    else:
        return bin_search_rec(arr, elem, start, mid)


def bin_search_iter(arr, elem):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2

        if arr[mid] == elem:
            return True
        elif elem > arr[mid]:
            start = mid + 1
        else:
            end = mid

    return False




if __name__ == '__main__':
    arr = [1, 4, 5, 6, 8, 10, 22]

    print(bin_search_rec(arr, 1, 0, len(arr)))
    print(bin_search_rec(arr, 11, 0, len(arr)))

    print(bin_search_iter(arr, 1))
    print(bin_search_iter(arr, 11))

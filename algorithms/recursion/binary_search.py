# (linear / tail-recursive) Recursive version
def binary_search_rec(arr, value, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if value == arr[mid]:
        return True
    elif value < arr[mid]:
        return binary_search_rec(arr, value, low, mid - 1)
    else:
        return binary_search_rec(arr, value, mid + 1, high)


# Since the binary search above is tail-recursive (it returns by calling the recursive function)
# It can also be very easily without recursion
def binary_search(arr, value):
    low = 0
    high = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if value == arr[mid]:
            return True
        elif value < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


array = [1, 2, 3, 4, 5, 6, 7]
print(binary_search_rec(array, 5, 0, len(array)))
print(binary_search(array, 5))

def binary_search(arr, value, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if value == arr[mid]:
        return True
    elif value < arr[mid]:
        return binary_search(arr, value, low, mid)
    else:
        return binary_search(arr, value, mid + 1, high)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    print(binary_search(array, 5, 0, len(array) - 1))
    print(binary_search(array, 9, 0, len(array) - 1))

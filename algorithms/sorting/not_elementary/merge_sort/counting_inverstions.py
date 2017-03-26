# https://www.hackerrank.com/challenges/ctci-merge-sort


def merge(array_low, array_high):
    result = []
    global sort_counter

    for i in range(0, len(array_low) + len(array_high)):

        if not array_high:
            result.append(array_low.pop(0))
            continue

        if not array_low:
            result.append(array_high.pop(0))
            continue

        if array_low[0] <= array_high[0]:
            result.append(array_low.pop(0))
            continue

        if array_high[0] < array_low[0]:
            sort_counter += len(array_low)
            result.append(array_high.pop(0))
            continue

    return result


def merge_sort(array):
    n = len(array)

    if n < 2:
        return array

    # divide
    mid = n // 2
    array_low = array[0: mid]
    array_high = array[mid: n]

    # conquer (with recursion)
    merge_sort(array_low)
    merge_sort(array_high)

    # merge results
    return merge(array_low, array_high)


def count_inversions(a):
    global sort_counter
    sort_counter = 0
    merge_sort(a)
    return sort_counter


if __name__ == "__main__":
    t = int(input().strip())

    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        print(count_inversions(arr))

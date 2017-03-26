# Plan:
#  - Divide the array into two halves
#  - Recursively sort each of the half
#  - Merge the two halves

# Divide and conquer, solve a problem by dividing it in two halves,
# solve the two halves and then put them together

# Time complexity: O(N log N)
# - N because of merge
# - log N because of divide and conquer sorting ( D(N) -> D(N/2) | D(N/2) -> D(N/4) | D(N/4) | D(N/4) | D(N/4) ....)

# Memory complexity: O(N)
# - We need the extra auxiliary array
# - It is very hard to do an in-place merge


def merge(array_low, array_high, merged_arr):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    low_index = 0
    high_index = 0

    while low_index + high_index < len(merged_arr):
        if high_index == len(array_high) or \
                (low_index < len(array_low) and array_low[low_index] < array_high[high_index]):
            merged_arr[low_index + high_index] = array_low[low_index]
            low_index += 1
        else:
            merged_arr[low_index + high_index] = array_high[high_index]
            high_index += 1

    return merged_arr


def merge_sort(array):
    """Sort the elements of Python list S using the merge-sort algorithm."""
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
    return merge(array_low, array_high, array)


if __name__ == "__main__":
    a = [5, 4, 2, 1, 3, 8, 6]
    print(a)
    print(merge_sort(a))

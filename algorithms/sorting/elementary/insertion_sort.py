# Move an index i from left to right
# in the i'th iteration, swap a[i] with each larger entity to its left
#
# Invariants:
# - entries to the left including the pointer are in ascending order
# - entries to the right have not been seen yet
#
# [1/4 * N^2] -> O(N^2) -> randomly order
# It does depend on the initial order of the data:
# - Best case:  the array is ordered => no exchanges just n-1 compares (Faster than selection sort)
# - Worst case: the array is in descending order => 1/2 * N^2 compares and 1/2 * N^2 exchanges
#   (Slower than selection sort) same compares but much more exchanges
#
# Interesting: Linear time for partially sorted arrays!
#
# Stable


def insertion_sort(array):
    # move th pointer to the right
    for i in range(len(array)):

        # put it on the right order
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break

    return array


# In place swap, faster
def ins_sort_no_swap(array):
    for i in range(len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array


if __name__ == "__main__":
    print(insertion_sort([5, 4, 2, 1, 3]))
    print(ins_sort_no_swap([5, 4, 2, 1, 3]))

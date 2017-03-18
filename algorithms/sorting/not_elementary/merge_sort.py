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


def merge(array, aux, low, mid, high):
    # Precondition: arr[low..mid] is sorted
    # Precondition: arr[mid+1..high] is sorted

    # copy all the elements into an auxiliary array
    for k in range(low, high):
        aux[k] = array[k]

    i = low
    j = mid + 1

    # accomplish the merging
    for k in range(low, high):

        # if the first part is exhausted, move the next j element
        if i > mid:
            array[k] = aux[j]
            j += 1

        # if the second part is exhausted, move the next j element
        elif j > high:
            array[k] = aux[i]
            i += 1

        # if the element in second part is larger than the element on the first part, copy this
        elif array[j] > array[i]:
            array[k] = aux[j]
            j += 1

        # if the element in first part is larger than the element on the second part, copy this
        else:
            array[k] = aux[i]
            i += 1

    # Post-condition: arr[low..high] is sorted


def sort(array, aux, low, high):
    # check if end
    if high <= low:
        return array

    # find the mid point
    mid = int(low + (high - low) / 2)

    # sort the left half
    sort(array, aux, low, mid)

    # sort the right half
    sort(array, aux, mid + 1, high)

    # merge them together
    merge(array, aux, low, mid, high)

    return array


def merge_sort(array):
    aux = [0] * len(array)
    return sort(array, aux, 0, len(array) - 1)


if __name__ == "__main__":
    print(merge_sort([5, 4, 2, 1, 3]))

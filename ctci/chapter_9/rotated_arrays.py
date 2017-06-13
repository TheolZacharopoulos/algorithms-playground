"""
Given a sorted array of n integers that has been rotated an unknown number of times,
write code to find an element in the array.
You may assume that the array was originally sorted in increasing order.

EXAMPLE
Input:
find 5 in {15, 16, 19, 20, 25, 1, 3 ,4 ,5 ,7 ,10, 14}

Output: 8 (the index of 5 in the array)
"""


def search(a, left, right, x):
    mid = (left + right) // 2

    if x == a[mid]:
        return mid

    if right < left:
        return -1

    # Either the left or right half must be normally ordered.
    # Find out which side is normally ordered, and then use the normally
    # ordered half to figure out which side to search to find x.

    # Left is normally ordered
    if a[left] < a[mid]:
        if a[left] <= x < a[mid]:
            return search(a, left, mid - 1, x)  # Search left
        else:
            return search(a, mid + 1, right, x)  # Search right

    # Right is normally ordered
    elif a[mid] < a[left]:
        if a[mid] < x <= a[right]:
            return search(a, mid + 1, right, x)  # Search right
        else:
            return search(a, left, mid - 1, x)  # Search left

    # Left or right half is all repeats
    elif a[left] == a[mid]:
        # If right is different, search it
        if a[mid] != a[right]:
            return search(a, mid + 1, right, x)  # Search right

        # Else, we have to search both halves
        else:
            result = search(a, left, mid - 1, x)  # Search left

            if result == -1:
                return search(a, mid + 1, right, x)  # Search right
            else:
                return result

    return -1


if __name__ == '__main__':
    array1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print(search(array1, 0, len(array1)-1, 5))

    array2 = [2, 2, 2, 2, 2, 2, 3, 3, 3, 1]
    print(search(array2, 0, len(array2)-1, 1))

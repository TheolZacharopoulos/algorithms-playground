"""
Given a sorted array of strings that is interspersed with empty strings,
write a method to find the location of a given string.

EXAMPLE
Input: ball, {"at", "", "", "", "ball", "" , "", "car", "", "", "dad", "", ""}
Output: 4
"""


def search(a, x):
    left = 0
    right = len(a)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] == "":
            left -= 1
        elif x > arr[mid]:
            left = mid + 1
        else:
            right = mid

    return -1


if __name__ == '__main__':
    arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]

    print(search(arr, "at"))
    print(search(arr, "ball"))
    print(search(arr, "car"))
    print(search(arr, "dad"))

"""
Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
This is easy if you use 0(n) space, where n is the length of the array.
However, you are required to solve it without allocating additional storage.

Sol:
For this problem, we can partition the array into three subarrays: Even, Unclassified, and Odd, appearing in that order.
Initially Even and Odd are empty, and Unclassified is the entire array.
We iterate through Unclassified, moving its elements to the boundaries of the Even and Odd subarrays via swaps,
thereby expanding Even and Odd, and shrinking Unclassified.

The additional space complexity is clearly 0(1),
a couple of variables that hold indices, and a temporary variable for performing the swap.
We do a constant amount of processing per entry, so the time complexity is 0(n).
"""


def even_odd(arr):
    next_even = 0
    next_odd = len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            temp = arr[next_even]
            arr[next_even] = arr[next_odd]
            arr[next_odd] = temp
            next_odd -= 1


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    even_odd(a)
    print(a)

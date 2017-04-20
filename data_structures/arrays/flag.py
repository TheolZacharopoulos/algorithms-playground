"""
Write a program that takes an array A and an index i into A,
and rearranges the elements such that all elements less than A[i] (the "pivot") appear first,
followed by elements equal to the pivot, followed by elements greater than the pivot.

The time complexity is 0(n) and the space complexity is 0(1).
"""


def dutch_flag(a, pivot_index):
    p = a[pivot_index]
    smaller = 0
    equal = 0
    larger = len(a) - 1

    while equal < larger:
        if a[equal] < p:
            a[equal], a[smaller] = a[smaller], a[equal]
            equal += 1
            smaller += 1
        elif a[equal] == p:
            equal += 1
        else:
            larger -= 1
            a[equal], a[larger] = a[larger], a[equal]


"""
Variant:
Given an array A of n objects with Boolean-valued keys,
reorder the array so that objects that have the key false appear first.
Use 0(1) additional space and 0(n) time.
"""


def dutch_flag_bools(a):
    next_false = 0
    next_true = len(a) - 1

    while next_false < next_true:
        if a[next_false] is False:
            next_false += 1
        else:
            a[next_false], a[next_true] = a[next_true], a[next_false]
            next_true -= 1


if __name__ == "__main__":
    arr = [3, 1, 7, 4, 6, 5, 7, 2, 7, 9, 8, 13]
    dutch_flag(arr, 2)
    print(arr)

    arr_bool = [True, True, False, True, False, False, True]
    dutch_flag_bools(arr_bool)
    print(arr_bool)

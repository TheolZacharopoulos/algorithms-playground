"""
 You are given an array-like data structure Listy which lacks a size method.
 It does, however, have an elementAt (i) method that returns the element at index i in 0(1) time.
 If i is beyond the bounds of the data structure, it returns - 1.
 (For this reason, the data structure only supports positive integers.)

 Given a Listy which contains sorted, positive integers, find the index at which an element x occurs.
 If x occurs multiple times, you may return any index.

 Solution:
 Could we compute the length? Yes!
 We know that elementAt will return -1 when i is too large.
 We can therefore just try bigger and bigger values until we exceed the size of the list.
 But how much bigger?

 If we just went through the list linearly: 1, then 2, then 3, then 4,
 and so on-we'd wind up with a linear time algorithm.
 We probably want something faster than this.
 Otherwise, why would the interviewer have specified the list is sorted?

 It's better to back off exponentially.
 Try 1, then 2, then 4, then 8, then 16, and so on.
 This ensures that, if the list has length n, we'll find the length in at most 0 (log n) time.
"""


class Listy:
    def __init__(self, elements):
        self.elements = elements

    def element_at(self, i):
        if i < len(self.elements):
            return self.elements[i]
        else:
            return -1


def binary_search(listy, value, low, high):
    while low <= high:
        mid = (low + high) // 2
        middle = listy.element_at(mid)

        if middle > value or middle == -1:
            high = mid - 1
        elif middle < value:
            low = mid + 1
        else:
            return mid
    return -1


def search(listy, value):
    index = 1
    while listy.element_at(index) != -1 and listy.element_at(index) < value:
        index *= 2

    return binary_search(listy, value, index // 2, index)


if __name__ == '__main__':
    l = Listy([1, 2, 4, 6, 7, 8, 12, 124])

    print(search(l, 4))

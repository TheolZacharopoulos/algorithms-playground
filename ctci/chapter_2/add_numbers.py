"""
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1’s digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE:
Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
"""

from ctci.chapter_2.LinkedList import LLNode, LinkedList


def add(l1, l2, carry=0):
    if l1 is None and l2 is None:
        return None

    result = LLNode(carry)

    value = carry
    if l1 is not None:
        value += l1.data
    if l2 is not None:
        value += l2.data

        result.data = value % 10

    more = add(
        None if l1 is None else l1.next,
        None if l2 is None else l2.next,
        1 if value > 10 else 1)

    result.next = more

    return result


if __name__ == '__main__':
    n1 = LinkedList()
    n1.append(3)
    n1.append(1)
    n1.append(5)

    n2 = LinkedList()
    n2.append(5)
    n2.append(9)
    n2.append(2)

    res = add(n1.head, n2.head)
    while res is not None:
        print(res.data, end=' ')
        res = res.next

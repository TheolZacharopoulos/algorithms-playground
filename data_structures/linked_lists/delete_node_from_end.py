"""
Given a singly linked list and an integer k, write a program to remove the kth last element from the list.
Your algorithm cannot use more than a few words of storage,
regardless of the length of the list.
In particular, you cannot assume that it is possible to record the length of the list.

Solution:
We use two iterators to traverse the list. The first iterator is advanced by k steps,
and then the two iterators advance in tandem.
When the first iterator reaches the tail, the second iterator is at the (k + l)th last node,
and we can remove the kth node.
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def delete_from_end(head, k):
    first = head

    while k > 0:
        first = first.next
        k -= 1

    second = head

    while first is not None:
        second = second.next
        first = first.next

    second.next = second.next.next

    return head

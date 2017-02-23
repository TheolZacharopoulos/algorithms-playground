# You’re given the pointer to the head node of a linked list and a specific position.
# Counting backwards from the tail node of the linked list, get the value of the node at the given position.
# A position of 0 corresponds to the tail, 1 corresponds to the node before the tail and so on.

# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


"""
 We have two pointers one is a iteration pointer and the other will be behind it by requested number of elements.
 Lets say we need to get value of 3rd element from tail.
 We start incrementing second pointer after 3rd element alongside with iteration pointer.
 When iteration pointer gets to the end(tail) second pointer is going to
 be pointing to 3rd element from it, which is our answer.
"""


def GetNode(head, position):
    if head is None:
        return

    # iteration pointer
    cur = head

    # resulting pointer
    res = head

    # keep an index which of the iteration
    index = 0

    while cur is not None:
        # in case index gets bigger than the position
        # then start moving the resulting pointer
        if index > position:
            res = res.next
        index += 1
        cur = cur.next

    # return resulting node's data
    return res.data

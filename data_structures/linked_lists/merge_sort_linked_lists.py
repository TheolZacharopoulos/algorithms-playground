# You’re given the pointer to the head nodes of two sorted linked lists.
# The data in both lists will be sorted in ascending order.
# Change the next pointers to obtain a single, merged linked list which also has data in ascending order.
# Either head pointer given may be null meaning that the corresponding list is empty.

# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def MergeLists(headA, headB):
    # Special case 1: None heads
    if headA is None:
        return headB

    if headB is None:
        return headA

    head = None

    # Special case 2: None nexts
    if headA.next is None and headB.next is None:
        if headA.data < headB.data:
            head = headA
            head.next = headB
        else:
            head = headB
            head.next = headA
        return head

    # Special case 3: Holds only for heads (not next)
    if headA.data < headB.data:
        head = headA
        headA = headA.next
    else:
        head = headB
        headB = headB.next

    cur = head
    while cur is not None:
        if headA.data < headB.data:
            cur.next = headA
            headA = headA.next
        else:
            cur.next = headB
            headB = headB.next

        cur = cur.next

        # Special case 4: Holds only for tails (next and next.next)
        if headA.next is None and headB.next is None:
            if headA.data < headB.data:
                cur.next = headA
                cur.next.next = headB
                break
            else:
                cur.next = headB
                cur.next.next = headA
                break

    return head


def MergeLists_Recursive(headA, headB):
    if headA is None:
        return headB

    if headA is None:
        return headA

    if headA.data < headB.data:
        headA.next = MergeLists_Recursive(headA.next, headB)
        return headA
    else:
        headB.next = MergeLists_Recursive(headB.next, headA)
        return headB

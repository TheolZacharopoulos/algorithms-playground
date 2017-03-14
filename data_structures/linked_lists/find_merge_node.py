# Given pointers to the head nodes of 2 linked lists that merge together at some point,
# find the Node where the two lists merge.
# It is guaranteed that the two head Nodes will be different, and neither will be NULL.

# https://www.youtube.com/watch?v=gE0GopCq378&t=238s


def list_len(head):
    cnt = 0
    cur = head
    while cur is not None:
        cnt += 1
        cur = cur.next
    return cnt


def FindMergeNode(headA, headB):
    lenA = list_len(headA)
    lenB = list_len(headB)

    # in case on of the lists is longer
    # find the difference and walk through that list
    # until the two lists are equal
    if lenA > lenB:
        diff = lenA - lenB
        for i in range(diff):
            headA = headA.next
    elif lenA < lenB:
        diff = lenB - lenA
        for i in range(diff):
            headB = headB.next

    # then just compare the values node by node
    while headA is not None and headB is not None:
        if headA.data == headB.data:
            return headA.data
        headA = headA.next
        headB = headB.next

    return None

# You're given the pointer to the head node of a sorted linked list,
# where the data in the nodes is in ascending order. Delete as few nodes as possible
# so that the list does not contain any value more than once. The given head pointer
# may be null indicating that the list is empty.


def RemoveDuplicates(head):
    if head is None:
        return None

    cur = head
    while cur is not None:
        # for many duplicated values in a row
        # remove until next is different
        while cur.next is not None and cur.data == cur.next.data:
            cur.next = cur.next.next
        cur = cur.next
    return head

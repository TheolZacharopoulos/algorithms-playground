"""
Write code to remove duplicates from an unsorted linked list.

FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
"""

from ctci.chapter_2.LinkedList import LLNode, LinkedList


def remove_duplicates(head):
    if head is None:
        return

    seen = [head.data]

    cur = head

    while cur.next is not None:
        if cur.next.data in seen:
            cur.next = cur.next.next
        else:
            seen.append(cur.next.data)
            cur = cur.next


def remove_duplicates_no_buf(head):
    if head is None:
        return

    prev = head
    current = prev.next

    while current is not None:
        runner = head

        # check for earlier duplicates
        while runner is not current:
            if runner.data == current.data:

                # remove current
                temp = current.next
                prev.next = temp

                # update current to the next node
                current = temp

                # all other duplicates have already been removed
                break
            runner = runner.next

            # current not updated - update now
            if runner is current:
                prev = current
                current = current.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.append(1)
    ll.append(3)
    ll.append(2)
    ll.append(4)
    ll.append(2)
    ll.append(4)

    for e in ll:
        print(e.data, end=' ')

    print("\n=============")

    # remove_duplicates(ll.head)
    remove_duplicates_no_buf(ll.head)

    for e in ll:
        print(e.data, end=' ')


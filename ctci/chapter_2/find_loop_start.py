"""
Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
DEFINITION:
Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an earlier node,
so as to make a loop in the linked list.

EXAMPLE:
Input: A -> B -> C -> D -> E -> C [the same C as earlier] Output: C
"""

from ctci.chapter_2.LinkedList import LLNode


def find_loop_start(head):
    slow = head
    fast = head

    # find meeting point
    while fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            break

    # error check: no meeting point therefore no loop
    if slow.next is None:
        return None

    # Move slow to Head. Keep fast at Meeting Point.
    # Each are k steps from the Loop Start.
    # If they move at the same pace, they must meet at Loop Start.
    slow = head

    while slow is not fast:
        slow = slow.next
        fast = fast.next

    # Now fast (& slow) points to the start of the loop.
    return fast


if __name__ == '__main__':
    a = LLNode('A')
    b = LLNode('B')
    c = LLNode('C')
    d = LLNode('D')
    e = LLNode('E')

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # cycle
    e.next = c

    print(find_loop_start(a))

# A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
# Complete the function provided for you in your editor.
# It has one parameter: a pointer to a Node object named  that points to the head of a linked list.
# Your function must return a boolean denoting whether or not there is a cycle in the list.
# If there is a cycle, return true; otherwise, return false.


def has_cycle(head):
    if head is None:
        return None

    cur = head
    prev = cur
    while cur is not None:
        if cur.next == prev:
            return True
        prev = cur
        cur = cur.next
    return False

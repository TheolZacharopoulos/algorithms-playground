# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Delete(head, position):
    if head is None:
        return None

    # if is about to remove head, change heads
    if position == 0:
        return head.next

    cur = head
    prev = head
    cnt = 0
    while cur is not None:
        if cnt == position:
            prev.next = cur.next
        prev = cur
        cur = cur.next
        cnt += 1

    if cnt != position:
        raise ValueError("Not enough nodes in the list!")

    return head


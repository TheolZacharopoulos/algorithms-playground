# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def InsertNth(head, data, position):
    new_node = Node(data)

    # if no head just return the new node
    if head is None:
        return new_node

    # if pos = 0, just prepend
    if position == 0:
        new_node.next = head
        return new_node

    # keep previous and next
    # set prev.next to new node, and current to new node
    cur = head
    prev = None
    cnt = 0
    while cnt < position:
        if cur.next is None:
            break
        prev = cur
        cur = cur.next
        cnt += 1

    if cnt != position:
        raise ValueError("Not enough nodes in the list!")

    new_node.next = cur

    # in case is not the last
    if prev is not None:
        prev.next = new_node

    return head


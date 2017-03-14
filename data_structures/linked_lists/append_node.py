# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    if head is None:
        return Node(data)
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = Node(data)
    return head

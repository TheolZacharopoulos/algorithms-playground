# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    if head is None:
        return Node(data)
    new_head = Node(data)
    new_head.next = head
    head = new_head
    return head


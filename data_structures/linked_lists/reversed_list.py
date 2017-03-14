# https://www.hackerrank.com/challenges/reverse-a-linked-list


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Reverse_Array(head):
    if head is None:
        return None

    nodes = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next

    for i in range(len(nodes) - 1, -1, -1):
        if i == 0:
            nodes[i].next = None
        else:
            nodes[i].next = nodes[i - 1]

    return nodes[len(nodes) - 1]


def Reverse_Recursive(head):
    if head is None or head.next is None:
        return head

    # reverse all but first
    new_head = Reverse_Recursive(head.next)

    # make original second point at first
    head.next.next = head

    # make original first point at nothing
    head.next = None

    return new_head

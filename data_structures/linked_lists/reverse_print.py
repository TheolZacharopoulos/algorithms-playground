# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def ReversePrintArray(head):
    if head is None:
        return

    values = []
    cur = head
    while cur is not None:
        values.append(cur.data)
        cur = cur.next

    for i in range(len(values) - 1, -1, -1):
        print(values[i])


def ReversePrintRecursive(head):
    if head is not None:
        ReversePrintRecursive(head.next)
        print(head.data)



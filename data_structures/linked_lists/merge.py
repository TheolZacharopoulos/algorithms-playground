"""
Consider two singly linked lists in which each node holds a number.
Assume the lists are sorted, i.e., numbers in the lists appear in ascending order within each list.
The merge of the two lists is a list consisting of the nodes of the two lists in which numbers appear in ascending order.
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        string = ""
        cur = self
        while cur is not None:
            string += str(cur.data)
            string += ","
            cur = cur.next
        string = string[:-1]

        return string


def merge(h1, h2):
    head = Node(0, None)
    cur = head
    p1 = h1
    p2 = h2

    while p1 is not None and p2 is not None:
        if p1.data <= p2.data:
            cur.next = p1
            p1 = p1.next
        else:
            cur.next = p2
            p2 = p2.next
        cur = cur.next

    # Appends the remaining nodes of pi or p2.
    if p1 is None:
        cur.next = p1
    else:
        cur.next = p2

    return head.next


if __name__ == '__main__':
    l1 = Node(2, Node(5, Node(7, None)))
    l2 = Node(3, Node(11, None))

    print(l1)
    print(l2)

    print(merge(l1, l2))

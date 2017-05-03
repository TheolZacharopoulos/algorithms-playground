"""
Write a program which takes a singly linked list L and two integers s and f as arguments,
and reverses the order of the nodes from the sth node to fth node, inclusive.
The numbering begins at 1, i.e., the head node is the first node. Do not allocate additional nodes.
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


def rev(head, s, f):
    # no need for reversing
    if s == f:
        return head

    dummy_head = Node(0, head)
    sublist_head = dummy_head

    cnt = 1
    while cnt < s:
        sublist_head = sublist_head.next
        cnt += 1

    # Reverse sublist.
    sublist_iter = sublist_head.next
    while s < f:
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
        s += 1

    return dummy_head.next


if __name__ == '__main__':
    l = Node(11, Node(3, Node(5, Node(7, Node(2, None)))))

    print(rev(l, 2, 4))

# https://www.hackerrank.com/challenges/compare-two-linked-lists


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


def CompareLists(headA, headB):
    if is_equal(headA, headB):
        return 1
    return 0


def is_equal(node_a, node_b):
    if node_a is None and node_b is not None:
        return False

    if node_a is not None and node_b is None:
        return False

    if node_a is None and node_b is None:
        return True

    if node_a.data != node_b.data:
        return False

    return is_equal(node_a.next, node_b.next)


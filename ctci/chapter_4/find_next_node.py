"""
Write an algorithm to find the ‘next’ node (e.g., in-order successor)
of a given node in a binary search tree where each node has a link to its parent.

1. If X has a right child, then the successor must be on the right side of X.
    Specifically, the left-most child must be the first node visited in that subtree.
2. Else, we go to X’s parent (call it P).
    2.a. If X was a left child (P.left = X), then P is the successor of X
    2.b. If X was a right child (P.right = X), then we have fully visited P, so we call successor(P).
"""


class NodeWithPar:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)


def successor(node):
    if node is None:
        return None

    # Case 1
    if node.parent is None or node.right is not None:
        return left_most_child(node.right)
    else:
        # Go up until we’re on left instead of right (case 2b)
        p = node.parent
        while p is not None:
            if p.left == node:
                break
            node = p
            p = node.parent

        return p


def left_most_child(node):
    if node is None:
        return None

    while node.left is not None:
        node = node.left

    return node

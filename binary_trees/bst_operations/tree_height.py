# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree
from binary_trees.bst_operations.BST import BSTNode


def height(root):
    """The height of a tree equals the height of its tallest subtree plus one."""

    if root is None or (root.get_left() is None and root.get_right() is None):
        return 0
    else:
        return 1 + max(height(root.get_left()), height(root.get_right()))


r = BSTNode(5,
            BSTNode(3,
                    BSTNode(2),
                    BSTNode(4)),

            BSTNode(7,
                    BSTNode(6),
                    BSTNode(8)))

print(height(r))

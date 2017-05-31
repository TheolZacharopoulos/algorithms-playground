"""
Implement a function to check if a tree is balanced.
For the purposes of this question, a balanced tree is defined to be a tree
such that no two leaf nodes differ in distance from the root by more than one.
"""

from ctci.chapter_4.BSTNode import BSTNode


def max_depth(node):
    if node is None:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))


def min_depth(node):
    if node is None:
        return 0
    return 1 + min(min_depth(node.left), min_depth(node.right))


def is_bst(root):
    return max_depth(root) - min_depth(root) <= 1


if __name__ == '__main__':
    r = BSTNode(2,
                BSTNode(1),
                BSTNode(3,
                        BSTNode(4)))

    print(is_bst(r))

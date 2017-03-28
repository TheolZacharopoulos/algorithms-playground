# https://www.hackerrank.com/challenges/tree-preorder-traversal
from data_structures.binary_trees.bst_operations.BST import BSTNode


def pre_order_recursive(root):
    if root is not None:
        # root first
        print(str(root.get_data()) + " ", end='')

        # left second
        pre_order_recursive(root.get_left())

        # right last
        pre_order_recursive(root.get_right())


def pre_order_iterative(root):
    stack = [root]

    while stack:
        v = stack.pop()

        print(str(v.get_data()) + " ", end='')

        # Push right child first
        # Emulate the recursive call stack
        if v.get_right() is not None:
            stack.append(v.get_right())

        if v.get_left() is not None:
            stack.append(v.get_left())

r = BSTNode(5,
            BSTNode(3,
                    BSTNode(2),
                    BSTNode(4)),

            BSTNode(7,
                    BSTNode(6),
                    BSTNode(8)))

pre_order_recursive(r)
print("")
pre_order_iterative(r)

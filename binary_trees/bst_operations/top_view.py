# https://www.hackerrank.com/challenges/tree-top-view
from binary_trees.bst_operations.BST import BSTNode


def go_left(node):
    if node.get_left() is not None:
        go_left(node.get_left())

    print(str(node.get_data()) + " ", end='')


def go_right(node):
    print(str(node.get_data()) + " ", end='')

    if node.get_right() is not None:
        go_right(node.get_right())


def top_view(root):
    if root.get_left() is not None:
        go_left(root.get_left())

    print(str(root.get_data()) + " ", end='')

    if root.get_right() is not None:
        go_right(root.get_right())


# More memory space?
def top_view_iterative(root):
    stack = []

    n = root
    while n is not None:
        stack.append(n.get_data())
        n = n.get_left()

    while stack:
        print(str(stack.pop()) + " ", end='')

    n = root
    while n is not None:
        n = n.get_right()

        if n is not None:
            print(str(n.get_data()) + " ", end='')


r = BSTNode(5,
            BSTNode(3,
                    BSTNode(2),
                    BSTNode(4)),

            BSTNode(7,
                    BSTNode(6),
                    BSTNode(8)))

top_view(r)
print("")
top_view_iterative(r)

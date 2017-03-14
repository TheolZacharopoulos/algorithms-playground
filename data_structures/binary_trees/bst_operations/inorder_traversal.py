# https://www.hackerrank.com/challenges/tree-inorder-traversal
# http://stackoverflow.com/a/2116755/4060931
from data_structures.binary_trees import BSTNode


def in_order_recursive(root):
    if root is not None:
        # left first
        in_order_recursive(root.get_left())

        # root second
        print(str(root.get_data()) + ' ', end='')

        # right last
        in_order_recursive(root.get_right())


def in_order_iterative(n):
    stack = []

    # Go to the end of the left side
    while n is not None:
        stack.append(n)
        n = n.get_left()

    while stack:
        v = stack.pop()

        print(str(v.get_data()) + ' ', end='')

        # get the right, and if there is:
        # put it in stack and get its left
        v = v.get_right()
        while v is not None:
            stack.append(v)
            v = v.get_left()


r = BSTNode(5,
            BSTNode(3,
                    BSTNode(2),
                    BSTNode(4)),

            BSTNode(7,
                    BSTNode(6),
                    BSTNode(8)))

in_order_recursive(r)
print("")
in_order_iterative(r)

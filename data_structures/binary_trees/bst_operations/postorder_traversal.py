# https://www.hackerrank.com/challenges/tree-postorder-traversal
from data_structures.binary_trees import BSTNode


def post_order_recursive(root):
    if root is not None:
        # left first
        post_order_recursive(root.get_left())

        # right second
        post_order_recursive(root.get_right())

        # root last
        print(str(root.get_data()) + " ", end='')


def post_order_iterative(n):
    stack = []

    # Go to the end of the left side
    while n is not None:
        stack.append(n)
        n = n.get_left()

    while stack:
        v = stack.pop()

        print(str(v.get_data()) + " ", end='')

        # root
        if not stack:
            return

        parent = stack[-1]
        right_child = parent.get_right()

        if v == right_child:
            continue

        v = right_child
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

post_order_recursive(r)
print("")
post_order_iterative(r)

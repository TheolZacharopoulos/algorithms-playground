# https://www.hackerrank.com/challenges/tree-level-order-traversal
from data_structures.binary_trees import BSTNode


def level_order_traversal_iterative(root):
    queue = []

    if root is not None:
        # enqueue
        queue.append(root)

    while queue:
        # dequeue
        n = queue.pop(0)

        print(str(n.get_data()) + " ", end='')

        if n.get_left() is not None:
            queue.append(n.get_left())

        if n.get_right() is not None:
            queue.append(n.get_right())


r = BSTNode(5,
            BSTNode(3,
                    BSTNode(2),
                    BSTNode(4)),

            BSTNode(7,
                    BSTNode(6),
                    BSTNode(8)))

level_order_traversal_iterative(r)

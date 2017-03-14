# https://www.hackerrank.com/challenges/binary-search-tree-insertion
from data_structures.binary_trees import BSTNode


def insert_rec(root, value):
    if root is None:
        return BSTNode(value)

    n_val = root.get_data()

    if value < n_val:
        if root.get_left() is None:
            root.set_left(BSTNode(value))
        else:
            insert_rec(root.get_left(), value)
    else:
        if root.get_right() is None:
            root.set_right(BSTNode(value))
        else:
            insert_rec(root.get_right(), value)


def insert_iterative(root, value):
    node = BSTNode(value)

    if root is not None:
        return node

    cur_root = node
    while True:
        if value < cur_root.get_data():
            if cur_root.get_left() is None:
                cur_root.set_left(node)
                break
            else:
                cur_root = cur_root.get_left()
        else:
            if cur_root.get_right() is None:
                cur_root.set_right(node)
                break
            else:
                cur_root = cur_root.get_right()

    return root

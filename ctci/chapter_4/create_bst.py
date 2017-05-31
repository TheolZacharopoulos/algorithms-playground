"""
Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.
"""


from ctci.chapter_4.BSTNode import BSTNode


def add_to_tree(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    node = BSTNode(arr[mid])

    node.left = add_to_tree(arr, start, mid - 1)
    node.right = add_to_tree(arr, mid + 1, end)

    return node


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]

    root = add_to_tree(a, 0, len(a) - 1)

    assert root.data == 4

    assert root.left.data == 2
    assert root.right.data == 6

    assert root.left.left.data == 1
    assert root.left.right.data == 3

    assert root.right.left.data == 5
    assert root.right.right.data == 7

# You are given a set of integers in an unordered binary tree.
# Use an array sorting routine to transform the tree into a heap that uses a
# balanced binary tree as its underlying data structure.
from binary_trees.bst_operations.BST import BSTNode


def traverse(node, count, arr=None):
    """Loads nodes into an array"""

    if node is None:
        return count

    if arr is not None:
        arr[count] = node

    count += 1
    count = traverse(node.get_left(), count, arr)
    count = traverse(node.get_right(), count, arr)

    return count


def heapify_binary_tree(root):
    # Two traversals:
    # 1. to count nodes
    size = traverse(root, 0)

    node_array = []

    # 2. to load nodes into the array
    traverse(root, 0, node_array)

    # Sort array of nodes based on their values
    sorted(node_array, key=lambda node: node.get_data())

    for i in range(size):
        left = 2*i + 1
        right = left + 1

        node_array[i].set_left(None if left >= size else node_array[left])
        node_array[i].set_right(None if right >= size else node_array[right])

    # Return new root node
    return node_array[0]

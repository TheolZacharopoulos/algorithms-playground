# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree
from binary_trees.bst_operations.BST import BSTNode


def height(root):
    """The height of a tree equals the height of its tallest subtree plus one."""

    if root is None or (root.get_left() is None and root.get_right() is None):
        return 0
    else:
        return 1 + max(height(root.get_left()), height(root.get_right()))


def height_iterative(root):
    if root is None:
        return 0

    node_stack = [root]
    depth_stack = [1]
    max_height = 0

    while len(node_stack) > 0:
        node = node_stack.pop()
        depth = depth_stack.pop()

        max_height = max_height if max_height > depth else depth

        if node.get_left() is not None:
            node_stack.append(node.get_left())
            depth_stack.append(depth + 1)

        if node.get_right() is not None:
            node_stack.append(node.get_right())
            depth_stack.append(depth + 1)

    return max_height

r = BSTNode(5,
            BSTNode(3,
                    BSTNode(2),
                    BSTNode(4)),

            BSTNode(7,
                    BSTNode(6),
                    BSTNode(8)))

print(height(r))
print(height_iterative(r))

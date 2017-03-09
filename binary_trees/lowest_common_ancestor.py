# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor
from binary_trees.bst_operations.BST import BSTNode


def lca(root, v1, v2):
    while root is not None:
        val = root.get_data()

        if val > v1 and val > v2:
            root = root.get_left()
        elif val < v1 and val < v2:
            root = root.get_right()
        else:
            return root
    return None


r = BSTNode(5,
            BSTNode(3,
                    BSTNode(2),
                    BSTNode(4)),

            BSTNode(7,
                    BSTNode(6),
                    BSTNode(8)))

print(lca(r, 6, 4))

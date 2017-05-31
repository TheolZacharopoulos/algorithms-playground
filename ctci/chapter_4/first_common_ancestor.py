"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.

Solutions:

Approach 1:
You could follow a chain in which p and q are on the same side.
That is, if p and q are both on the left of the node, branch left to look for the common ancestor.
When p and q are no longer on the same side, you must have found the first common ancestor.

Approach 2:
For any node r, we know the following:
1. If p is on one side and q is on the other, r is the first common ancestor.
2. Else, the first common ancestor is on the left or the right side.

So, we can create a simple recursive algorithm called search that calls search(left side) and search(right side)
looking at how many nodes (p or q) are placed from the left side and from the right side of the current node.

- If there are two nodes on one of the sides, then we have to check if the child node on this side is p or q
(because in this case the current node is the common ancestor).

- If the child node is neither p nor q, we should continue to search further (starting from the child).

- If one of the searched nodes (p or q) is located on the right side of the current node,
then the other node is located on the other side. Thus the current node is the common ancestor.

Approach 3:
Find paths for p and q, returns them as a stack of nodes of the path
and find where they diverge (where is the last common node).
https://www.youtube.com/watch?v=GnliEfQo114
"""

from ctci.chapter_4.BSTNode import BSTNode


# Approach 1

def is_child_of(root, p):
    """
    is p a child of root?
    """

    if root is None:
        return False

    if root is p:
        return True

    return is_child_of(root.left, p) or is_child_of(root.right, p)


def first_common_ancestor(root, p, q):
    if is_child_of(root.left, p) and is_child_of(root.left, q):
        return first_common_ancestor(root.left, p, q)

    if is_child_of(root.right, p) and is_child_of(root.right, q):
        return first_common_ancestor(root.right, p, q)

    return root


# Approach 3
def path_to(root, p):
    if root is None:
        return None

    if root == p:
        return [p]

    left = path_to(root.left, p)
    if left is not None:
        left.append(root)
        return left

    right = path_to(root.right, p)
    if right is not None:
        right.append(root)
        return right

    return None


def lca(root, p, q):
    path_to_p = path_to(root, p)
    path_to_q = path_to(root, q)

    node = None
    while path_to_p and path_to_q:
        node_p = path_to_p.pop()
        node_q = path_to_q.pop()

        if node_p == node_q:
            node = node_q
        else:
            break

    return node


if __name__ == '__main__':
    root = BSTNode(4,
                   BSTNode(2,
                           BSTNode(1),
                           BSTNode(3)),
                   BSTNode(6,
                           BSTNode(5),
                           BSTNode(7))
                   )

    print(first_common_ancestor(root, root.left, root.right))
    print(first_common_ancestor(root, root.left.left, root.left.right))

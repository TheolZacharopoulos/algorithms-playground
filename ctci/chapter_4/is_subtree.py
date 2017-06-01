"""
You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes.
Create an algorithm to decide if T2 is a subtree of T1.

Solution:
The treeMatch procedure visits each node in the small tree at most once and
is called no more than once per node of the large tree.
Worst case runtime is at most O(n * m), where n and m are the sizes of trees T1 and T2, respectively.
If k is the number of occurrences of T2’s root in T1, the worst case runtime can be characterized as O(n + k * m).
"""


def contains_tree(t1, t2):
    if t2 is None:
        return True
    else:
        return sub_tree(t1, t2)


def sub_tree(r1, r2):
    # big tree empty & subtree still not found.
    if r1 is None:
        return False

    if r1.data == r2.data:
        if match_tree(r1, r2):
            return True

    return sub_tree(r1.left, r2) or sub_tree(r1.right, r2)


def match_tree(r1, r2):
    # nothing left in the subtree
    if r1 is None and r2 is None:
        return True

    # big tree empty & subtree still not found
    if r1 is None or r2 is None:
        return False

    # data doesn't match
    if r1.data != r2.data:
        return False

    return match_tree(r1.left, r2.left) and match_tree(r1.right, r2.right)

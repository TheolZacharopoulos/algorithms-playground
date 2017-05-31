"""
Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth
(eg, if you have a tree with depth D, you’ll have D linked lists).

In a usual breath first search traversal, we simply traverse the nodes without caring which level we are on.
In this case, it is critical to know the level.
We thus use a dummy node to indicate when we have finished one level and are starting on the next.
"""

from ctci.chapter_4.BSTNode import BSTNode


def create_linked_lists(root):
    level = 0
    result = []

    l = [root]
    result.insert(level, l)

    while True:
        l = []

        for i in range(0, len(result[level])):
            n = result[level][i]

            if n is not None:
                if n.left is not None:
                    l.append(n.left)
                if n.right is not None:
                    l.append(n.right)

        if len(l) > 0:
            result.insert(level + 1, l)
        else:
            break
        level += 1

    return result

if __name__ == '__main__':
    root = BSTNode(4,
                   BSTNode(2,
                           BSTNode(1),
                           BSTNode(3)),
                   BSTNode(6,
                           BSTNode(5),
                           BSTNode(7))
                   )

    lls = create_linked_lists(root)

    for ll in lls:
        for e in ll:
            print(str(e) + " ", end='')
        print("")

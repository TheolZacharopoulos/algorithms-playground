# https://www.hackerrank.com/challenges/tree-huffman-decoding


class Node:
    def __init__(self, data=None, freq=None, left=None, right=None):
        self.data = data
        self.freq = freq
        self.left = left
        self.right = right


def decode(root, s):
    n = root

    for c in s:
        if c == '1':
            # go to the right
            n = n.right
        else:
            # go to the left
            n = n.left

        if n.left is None and n.right is None:
            print(str(n.data), end='')

            # its a leaf, reset to root
            n = root


huffman_tree = Node(None, 5,
                    Node(None, 2,
                         Node('B', 1, None, None),
                         Node('C', 1, None, None)),
                    Node('A', 3, None, None))

decode(huffman_tree, "1001011")

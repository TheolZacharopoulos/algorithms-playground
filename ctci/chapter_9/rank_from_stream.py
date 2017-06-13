"""
Imagine you are reading in a stream of integers.
Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal to x).
Implement the data structures and algorithms to support these operations.
That is, implement the method track(int x), which is called when each number is generated,
and the method getRankOfNumber(int x),
which returns the number of values less than or equal to x (not including x itself).

SOLUTION:
A relatively easy way to implement this would be to have an array that holds all the elements in sorted order.
When a new element comes in, we would need to shift the other elements to make room.
Implementing getRankOfNumber would be quite efficient, though.
We would simply perform a binary search for n, and return the index.

However, this is very inefficient for inserting elements (that is, the track(int x) function).
We need a data structure which is good at keeping relative ordering, as well as updating when we insert new elements.

A binary search tree can do just that.
Instead of inserting elements into an array, we insert elements into a binary search tree.
The method track(int x) will run in 0(log n) time,
To find the rank of a number, we could do an in-order traversal, keeping a counter as we traverse.
The goal is that, by the time we find x, counter will equal the number of elements less than x.

As long as we're moving left during searching for x, the counter won't change.
Why? Because all the values we're skipping on the right side are greater than x.
After all, the very smallest element (with rank of 1) is the leftmost node.

When we move to the right though, we skip over a bunch of elements on the left.
All of these elements are less than x, so we'll need to increment counter by the number of elements in the left subtree.
Rather than counting the size of the left subtree (which would be inefficient),
we can track this information as we add new elements to the tree.

int getRank(Node node, int x) {
    if x is node.data, return node.leftSize()
    if x is on left of node, return getRank(node.left, x)
    if x is on right of node, return node.leftSize() + 1 + getRank(node.right, x)
}
"""


class RankNode:
    def __init__(self, data):
        self.data = data
        self.left_size = 0
        self.left = None
        self.right = None

    def insert(self, d):
        if d <= self.data:
            if self.left is not None:
                self.left.insert(d)
            else:
                self.left = RankNode(d)
                self.left_size += 1
        else:
            if self.right is not None:
                self.right.insert(d)
            else:
                self.right = RankNode(d)

    def get_rank(self, d):
        if d == self.data:
            return self.left_size
        elif d < self.data:
            if self.left is None:
                return -1
            else:
                return self.left.get_rank(d)
        else:
            right_rank = -1 if self.right is None else self.right.get_rank(d)

            if right_rank == -1:
                return -1
            else:
                return self.left_size + 1 + right_rank


root = None


def track(number):
    if root is None:
        return RankNode(number)
    else:
        root.insert(number)


def get_rank_of_num(number):
    return root.get_rank(number)

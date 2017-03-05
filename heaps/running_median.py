# https://www.hackerrank.com/challenges/find-the-running-median


class MinHeap:
    def __init__(self):
        # start from element 1 (root)
        self.array = [None]

    def __str__(self):
        return str(self.array)

    def swap(self, index_a, index_b):
        temp = self.array[index_a]
        self.array[index_a] = self.array[index_b]
        self.array[index_b] = temp

    def swim(self, index):
        """
         Promote a node up to the binary tree
        """
        # while it is not the root, and the parent is smaller than this node
        # promote the node up to to the tree
        while index > 1 and self.array[int(index / 2)] >= self.array[index]:
            self.swap(index, int(index / 2))
            index = int(index / 2)

    def insert(self, data):
        # Add the new element at the end of the heap
        self.array.append(data)

        # Keep the heap in order by promoting the new node at the correct place
        last_index = len(self.array) - 1
        self.swim(last_index)

    def sink(self, index):
        """
        Put a node down of the binary tree
        """
        while 2 * index < len(self.array):
            # left child is smaller
            smaller_child = 2 * index

            # right child is smaller
            if smaller_child < (len(self.array) - 1) and self.array[smaller_child] > self.array[smaller_child + 1]:
                smaller_child += 1

            # order fixed
            if self.array[index] < self.array[smaller_child]:
                break

            self.swap(index, smaller_child)

            index = smaller_child

    def del_min(self):
        # root is always the min
        min_element = self.array[1]

        # make the last element as root
        self.swap(1, len(self.array) - 1)
        del self.array[len(self.array) - 1]

        # put the heap in the right order
        self.sink(1)

        return min_element

    def peek(self):
        return self.array[1]

    def is_empty(self):
        return len(self.array) == 1

    def size(self):
        return len(self.array) -1


class MaxHeap:
    def __init__(self):
        # start from element 1 (root)
        self.array = [None]

    def __str__(self):
        return str(self.array)

    def swap(self, index_a, index_b):
        temp = self.array[index_a]
        self.array[index_a] = self.array[index_b]
        self.array[index_b] = temp

    def swim(self, index):
        """
         Promote a node up to the binary tree
        """
        # while it is not the root, and the parent is smaller than this node
        # promote the node up to to the tree
        while index > 1 and self.array[int(index / 2)] < self.array[index]:
            self.swap(index, int(index / 2))
            index = int(index / 2)

    def insert(self, data):
        # Add the new element at the end of the heap
        self.array.append(data)

        # Keep the heap in order by promoting the new node at the correct place
        last_index = len(self.array) - 1
        self.swim(last_index)

    def sink(self, index):
        """
        Put a node down of the binary tree
        """
        while 2 * index < len(self.array):
            # left child is smaller
            smaller_child = 2 * index

            # right child is smaller
            if smaller_child < (len(self.array) - 1) and self.array[smaller_child] < self.array[smaller_child + 1]:
                smaller_child += 1

            # order fixed
            if self.array[index] >= self.array[smaller_child]:
                break

            self.swap(index, smaller_child)

            index = smaller_child

    def del_max(self):
        # root is always the max
        max_element = self.array[1]

        # make the last element as root
        self.swap(1, len(self.array) - 1)
        del self.array[len(self.array) - 1]

        # put the heap in the right order
        self.sink(1)

        return max_element

    def peek(self):
        return self.array[1]

    def size(self):
        return len(self.array) - 1


def get_median(e, m, l, r):
    """
    We can use a max heap on left side to represent elements that are less than effective median,
    and a min heap on right side to represent elements that are greater than effective median.
    After processing an incoming element, the number of elements in heaps differ utmost by 1 element.
    When both heaps contain same number of elements, we pick average of heaps root data as effective median.
    When the heaps are not balanced, we select effective median from the root of heap containing more elements.
    """

    # The left and right heaps contain same number of elements
    if l.size() == r.size():

        # current element fits in left (max) heap
        if e < m:
            l.insert(e)
            m = l.peek()
        else:
            # current element fits in right(min) heap
            r.insert(e)
            m = r.peek()

    # There are more elements in left (max) heap
    elif l.size() > r.size():

        # current element fits in left (max) heap
        if e < m:
            # Remove top element from left heap and
            # insert into right heap
            r.insert(l.del_max())

            # current element fits in left (max) heap
            l.insert(e)
        else:
            # current element fits in right (min) heap
            r.insert(e)

        # Both heaps are balanced
        m = (l.peek() + r.peek()) / 2

    # There are more elements in right (min) heap
    elif r.size() > l.size():
        # current element fits in left (max) heap
        if e < m:
            l.insert(e)
        else:
            # Remove top element from right heap and
            # insert into left heap
            l.insert(r.del_min())

            # current element fits in right (min) heap
            r.insert(e)

        # Both heaps are balanced
        m = (l.peek() + r.peek()) / 2

    return m


left = MaxHeap()
right = MinHeap()
median = float("inf")

n = int(input().strip())

for i in range(n):
    elem = int(input().strip())
    median = get_median(elem, median, left, right)
    print("%2.1f" % median)

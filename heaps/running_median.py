# https://www.hackerrank.com/challenges/find-the-running-median


class Heap:
    def __init__(self):
        # start from element 1 (root)
        self.array = [None]

    def extract_top(self):
        pass

    def swap(self, index_a, index_b):
        temp = self.array[index_a]
        self.array[index_a] = self.array[index_b]
        self.array[index_b] = temp

    def __str__(self):
        return str(self.array)

    def peek(self):
        return self.array[1]

    def is_empty(self):
        return len(self.array) == 1

    def size(self):
        return len(self.array) -1


class MinHeap(Heap):
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

    def extract_top(self):
        # root is always the min
        min_element = self.array[1]

        # make the last element as root
        self.swap(1, len(self.array) - 1)
        del self.array[len(self.array) - 1]

        # put the heap in the right order
        self.sink(1)

        return min_element


class MaxHeap(Heap):
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

    def extract_top(self):
        # root is always the max
        max_element = self.array[1]

        # make the last element as root
        self.swap(1, len(self.array) - 1)
        del self.array[len(self.array) - 1]

        # put the heap in the right order
        self.sink(1)

        return max_element


class RunningMedian:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def add(self, item):
        """
        If the item is greater than or equal to the max element of the max heap
        it surely belongs to the min heap, otherwise to the max heap.
        """
        if self.max_heap.size() > 0 and item >= self.max_heap.peek():
            self.min_heap.insert(item)
        else:
            self.max_heap.insert(item)

        # Balance the heaps (keep the the same size)
        if abs(self.max_heap.size() - self.min_heap.size()) > 1:
            if self.max_heap.size() > self.min_heap.size():
                self.min_heap.insert(self.max_heap.extract_top())
            else:
                self.max_heap.insert(self.min_heap.extract_top())

    def get_median(self):
        total = self.min_heap.size() + self.max_heap.size()

        # it is even
        if total % 2 == 1:
            if self.max_heap.size() > self.min_heap.size():
                return self.max_heap.peek()
            else:
                return self.min_heap.peek()

        # it is odd
        else:
            ret = 0
            if not self.max_heap.is_empty():
                ret += self.max_heap.peek()

            if not self.min_heap.is_empty():
                ret += self.min_heap.peek()

            ret /= 2

            return ret


running_median = RunningMedian()

n = int(input().strip())

for i in range(n):
    elem = int(input().strip())
    running_median.add(elem)
    median = running_median.get_median()
    print("%2.1f" % median)

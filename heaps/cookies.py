# https://www.hackerrank.com/challenges/jesse-and-cookies


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


def count_operations(array, k):
    heap = MinHeap()

    for item in array:
        heap.insert(item)

    ops_cnt = 0
    min_sweet = heap.peek()

    while min_sweet < k and not heap.is_empty():
        min_1 = heap.del_min()

        if heap.is_empty():
            return -1

        min_2 = heap.del_min()

        heap.insert((1 * min_1) + (2 * min_2))
        min_sweet = heap.peek()
        ops_cnt += 1

    if heap.is_empty():
        return -1
    else:
        return ops_cnt

n, k = input().strip().split(' ')
arr = [int(i) for i in input().strip().split(' ')]

print(count_operations(arr, int(k)))

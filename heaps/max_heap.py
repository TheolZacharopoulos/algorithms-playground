class MaxHeap:
    def __init__(self):
        # start from element 1 (root)
        self.array = [None]

    def __str__(self):
        return str(self.array)

    def get_parent(self, index):
        return self.array[int(index / 2)]

    def get_left_child(self, index):
        return self.array[int(2 * index)]

    def get_right_child(self, index):
        return self.array[int(2 * index) + 1]

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
        while index > 1 and self.get_parent(index) < self.array[index]:
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

heap = MaxHeap()

print(heap)

heap.insert(2)
print(heap)

heap.insert(1)
print(heap)

heap.insert(3)
print(heap)

heap.insert(5)
print(heap)

heap.insert(4)
print(heap)

heap.del_max()
print(heap)

heap.del_max()
print(heap)

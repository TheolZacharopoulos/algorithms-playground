class FixedSizeStack:
    def __init__(self, capacity):
        self.array = [0] * capacity
        self.size = 0

    def push(self, data):
        self.array[self.size] = data
        self.size += 1

    def pop(self):
        item = self.array[self.size-1]

        del self.array[self.size-1]
        self.size -= 1

        return item

    def is_empty(self):
        return self.size == 0


# Repeated doubling technique
class ResizingStack:
    def __init__(self):
        self.array = [0]
        self.size = 0

    def push(self, data):
        if self.size == len(self.array):
            self.resize(2 * len(self.array))

        self.array[self.size] = data
        self.size += 1

    def pop(self):
        item = self.array[self.size - 1]
        self.size -= 1

        self.array[self.size] = None

        if self.size > 0 and self.size == len(self.array)/4:
            self.resize(len(self.array) / 2)

        return item

    def resize(self, capacity):
            copy_arr = [0] * int(capacity)
            for i in range(self.size):
                copy_arr[i] = self.array[i]
            self.array = copy_arr

s = FixedSizeStack(3)

s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()

print(s.array)


s = ResizingStack()

s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()

print(s.array)

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

s = FixedSizeStack(3)

s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()

print(s.array)

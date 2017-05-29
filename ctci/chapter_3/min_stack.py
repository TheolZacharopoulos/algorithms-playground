"""
How would you design a stack which, in addition to push and pop,
also has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.
"""

from ctci.chapter_3.LLStack import Stack


class MinStack(Stack):
    def __init__(self):
        super().__init__()

        self.s2 = Stack()

    def push(self, item):
        if item < self.min():
            self.s2.push(item)

        super().push(item)

    def pop(self):
        item = super().pop()

        if item is self.min():
            self.s2.pop()

        return item

    def min(self):
        if self.s2.is_empty():
            return float('inf')
        else:
            return self.s2.peek()


if __name__ == '__main__':
    s = MinStack()

    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)

    print(s.min())
    print(s.min())

    s.pop()
    print(s.min())

    s.pop()
    print(s.min())

    s.pop()
    print(s.min())

"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.

Implement a data structure SetOfStacks that mimics this.
SetOfStacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).
"""

from ctci.chapter_3.LLStack import Stack


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1]

    def push(self, item):
        last_stack = self.get_last_stack()
        if last_stack is not None and len(last_stack) is not self.capacity:
            last_stack.push(item)
        else:
            stack = Stack()
            stack.push(item)
            self.stacks.append(stack)

    def pop(self):
        last_stack = self.get_last_stack()

        if last_stack is None:
            raise Exception("ERROR: No more elements")

        item = last_stack.pop()

        if len(last_stack) == 0:
            self.stacks.pop()

        return item


if __name__ == '__main__':
    s = SetOfStacks(2)

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

    try:
        print(s.pop())
    except Exception as s:
        print(s)

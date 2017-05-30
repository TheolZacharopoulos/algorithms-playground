"""
Implement a MyQueue class which implements a queue using two stacks.
"""


from ctci.chapter_3.LLStack import Stack


class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if not self.s2.is_empty():
            return self.s2.pop()

        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())

        return self.s2.pop()


if __name__ == '__main__':
    s = MyQueue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)

    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())

    try:
        print(s.dequeue())
    except Exception as s:
        print(s)

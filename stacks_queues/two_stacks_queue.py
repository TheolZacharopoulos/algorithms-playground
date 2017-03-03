# https://www.hackerrank.com/challenges/queue-using-two-stacks


class TwoStackQueue:
    def __init__(self):
        self.temp_stack = list()
        self.stack = list()

    def enqueue(self, data):
        self.temp_stack.clear()

        # if the queue is empty, just add the item
        if self.is_empty():
            self.stack.append(data)
        else:

            # empty stack 2 into the stack 1
            while len(self.stack) > 0:
                self.temp_stack.append(self.stack.pop())

            # add the new item at the top
            self.temp_stack.append(data)

            # empty stack 1 back into the stack 2 (correct order)
            while len(self.temp_stack) > 0:
                self.stack.append(self.temp_stack.pop())

    def dequeue(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def front(self):
        return self.stack[len(self.stack)-1]

    def __str__(self):
        return str(self.stack)

n = int(input())

queue = TwoStackQueue()

for i in range(n):
    inp = input().strip().split(' ')

    if inp[0] == '1':
        queue.enqueue(inp[1])

    if inp[0] == '2':
        queue.dequeue()

    if inp[0] == '3':
        print(queue.front())

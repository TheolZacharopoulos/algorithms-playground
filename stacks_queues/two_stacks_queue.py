# https://www.hackerrank.com/challenges/queue-using-two-stacks

# Logic :
# Always enqueue to enqueue_stack.
# Always dequeue from dequeue_stack (point 3 if empty).
# Transfer all elements from enqueue_stack to dequeue_stack if dequeue_stack is empty (if need to dequeue).


class MyQueue(object):
    def __init__(self):
        self.dequeue_stack = []
        self.enqueue_stack = []
        self.first = None

    def peek(self):
        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack[-1]
        else:
            return self.first

    def put(self, value):
        if len(self.enqueue_stack) == 0:
            self.first = value
        self.enqueue_stack.append(value)

    def pop(self):
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        self.dequeue_stack.pop()


queue = MyQueue()

t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())


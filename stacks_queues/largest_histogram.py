# https://www.hackerrank.com/challenges/largest-rectangle
# https://www.youtube.com/watch?v=ZmnqCZp9bBs
# https://www.youtube.com/watch?v=VNbkzsnllsU


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        old_head = self.head
        self.head = Node(data)
        self.head.next = old_head

    def pop(self):
        item = self.head
        self.head = self.head.next
        return item.data

    def is_empty(self):
        return self.head is None

    def top(self):
        return self.head.data


def largest_histogram(hist):
    stack = Stack()
    max_area = 0
    area = 0
    i = 0

    while i < len(hist):
        if stack.is_empty() or hist[stack.top()] <= hist[i]:
            stack.push(i)
            i += 1
        else:
            top = stack.pop()

            # if stack is empty means everything till i has to be
            # greater or equal to input[top] so get area by hist[top] * i;
            if stack.is_empty():
                area = hist[top] * i

            # if stack is not empty then everything from i-1 to hist.peek() + 1
            # has to be greater or equal to hist[top]
            # so area = hist[top] * (i - stack.peek() - 1);
            else:
                area = hist[top] * (i - stack.top() - 1)

            if area > max_area:
                max_area = area

    while not stack.is_empty():
        top = stack.pop()
        # if stack is empty means everything till i has to be
        # greater or equal to hist[top] so get area by hist[top] * i;
        if stack.is_empty():
            area = hist[top] * i

        # if stack is not empty then everything from i-1 to hist.peek() + 1
        # has to be greater or equal to input[top]
        # so area = hist[top] * (i - stack.peek() - 1);
        else:
            area = hist[top] * (i - stack.top() - 1)

        if area > max_area:
            max_area = area

    return max_area


N = int(input().strip())

h = [int(i) for i in input().strip().split(' ')]

print(largest_histogram(h))

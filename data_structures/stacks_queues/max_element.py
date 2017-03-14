# https://www.hackerrank.com/challenges/maximum-element


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class MaxStack:
    def __init__(self):
        self.head = None
        self.max_element = 0

    def push(self, data):
        old_head = self.head
        self.head = Node(data)
        self.head.next = old_head

    def pop(self):
        item = self.head
        self.head = self.head.next
        return item.data

    def push_max(self, data):
        if data < self.max_element:
            self.push(data)
        else:
            self.push(data + self.max_element)
            self.max_element = data

    def pop_max(self):
        data = self.pop()
        if data < self.max_element:
            return data
        else:
            self.max_element = data - self.max_element
            return self.max_element

    def is_empty(self):
        return self.head is None

    def get_max(self):
        return self.max_element


s = MaxStack()

N = int(input().strip())

for q in range(N):
    inp = input().strip().split(' ')
    t = inp[0]

    if len(inp) > 1:
        x = inp[1]

    if t == '1':
        s.push_max(int(x))

    if t == '2':
        s.pop_max()

    if t == '3':
        print(s.get_max())


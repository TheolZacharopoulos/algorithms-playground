class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


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
        return item

    def is_empty(self):
        return self.head is None

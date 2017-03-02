class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        old_tail = self.tail
        self.tail = Node(data)

        if self.is_empty():
            self.head = self.tail
        else:
            old_tail.next = self.tail

    def dequeue(self):
        item = self.head.data
        self.head = self.head.next

        if self.is_empty():
            self.tail = None

        return item

    def is_empty(self):
        return self.head is None

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()

print(q.head)

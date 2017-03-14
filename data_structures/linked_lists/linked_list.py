class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)

        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = Node(data)

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head

        self.head = new_head

    def delete(self, data):
        if self.head is Node:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next is not Node:
            if cur.next.data == data:
                cur.next = cur.next.next
                return
            else:
                cur = cur.next

class LLNode:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

    def __eq__(self, other):
        return self.data == self.data and self.next == self.next

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = LLNode(data)
            return

        # go to the end of the list
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = LLNode(data)

    def prepend(self, data):
        if self.head is None:
            self.head = LLNode(data)
            return

        new_head = LLNode(data)

        new_head.next = self.head
        self.head = new_head

    def delete_with_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next is not None:
            if cur.next.data == data:
                cur.next = cur.next.next
                return
            cur = cur.next

    def find_node(self, data):
        if self.head is None:
            return None

        cur = self.head

        while cur is not None:
            if cur.data == data:
                return cur
            cur = cur.next

        return None

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next

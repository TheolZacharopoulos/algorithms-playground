from ctci.chapter_2.LinkedList import LLNode


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def pop(self):
        if self.top is None:
            raise Exception("ERROR: Out of index")

        item = self.top.data
        self.top = self.top.next

        self.length -= 1

        return item

    def push(self, item):
        if self.top is None:
            self.top = LLNode(item)
        else:
            new_top = LLNode(item, self.top)
            self.top = new_top

        self.length += 1

    def peek(self):
        return self.top.data

    def is_empty(self):
        return self.top is None

    def __len__(self):
        return self.length

    def __iter__(self):
        cur = self.top

        while cur is not None:
            yield cur.data
            cur = cur.next

    def __eq__(self, other):
        while self.top is not None and other.top is not None:
            if self.top is not other.top:
                return False

        return True


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.pop())
    print(s.pop())
    print(s.pop())

    try:
        print(s.pop())
    except Exception as s:
        print(s)



from ctci.chapter_2.LinkedList import LLNode


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def enqueue(self, item):
        if self.front is None:
            self.back = LLNode(item)
            self.front = self.back
        else:
            self.back.next = LLNode(item)
            self.back = self.back.next

        self.length += 1

    def dequeue(self):
        if self.front is None:
            raise Exception("ERROR: Out of index")

        item = self.front.data
        self.front = self.front.next

        self.length -= 1

        return item

    def __len__(self):
        return self.length


if __name__ == '__main__':
    s = Queue()
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

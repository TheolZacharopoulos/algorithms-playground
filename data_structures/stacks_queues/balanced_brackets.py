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
        return item

    def is_empty(self):
        return self.head is None


def is_balanced(string):
    stack = Stack()
    s = list(string)

    for c in s:
        if c == '{' or c == '[' or c == '(':
            stack.push(c)

        if stack.is_empty():
            return "NO"
        elif c == '}':
            node = stack.pop()
            if node.data != '{':
                return "NO"
        elif c == ']':
            node = stack.pop()
            if node.data != '[':
                return "NO"
        elif c == ')':
            node = stack.pop()
            if node.data != '(':
                return "NO"

    if stack.is_empty():
        return "YES"
    else:
        return "NO"


t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    print(is_balanced(s))

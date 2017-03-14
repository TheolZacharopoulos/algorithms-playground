class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Push data at the head of the stack
        :param data: the data to be added
        :return: True if it succeed
        """
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        return True

    def pop(self):
        """
        Pops data from the head of the list
        :return: the head's data
        """
        if self.head is None:
            return None
        element = self.head
        self.head = self.head.next
        return element.data

    def delete_stack(self):
        """
        Deletes a whole stack
        :return: True if it succeed
        """
        self.head = None

        # or could pop repeatedly:
        # while self.head is not None:
        #     pop()

    def __str__(self):
        return str(self.head)


stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
print(stack)
stack.push(3)
stack.push(4)
stack.pop()
print(stack)
stack.pop()
print(stack)


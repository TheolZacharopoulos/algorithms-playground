class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


def has_cycle(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while True:
        if fast is None or fast.next is None:
            return False
        elif fast == slow or fast.next == slow:
            return True
        slow = slow.next
        fast = fast.next.next


n1_cycle = Node(1)
n2_cycle = Node(2)
n3_cycle = Node(3)

n1_cycle.next = n2_cycle
n2_cycle.next = n3_cycle
n3_cycle.next = n2_cycle

print(has_cycle(n1_cycle) is True)

n1_no_cycle = Node(1)
n2_no_cycle = Node(2)
n3_no_cycle = Node(3)

n1_no_cycle.next = n2_no_cycle
n2_no_cycle.next = n3_no_cycle

print(has_cycle(n1_no_cycle) is False)

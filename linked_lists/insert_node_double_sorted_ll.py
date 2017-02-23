# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list


class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.data) + " <--> " + str(self.next)


def SortedInsert(head, data):
    if head is None:
        return None

    new_node = Node(data)

    # if it goes to the head
    if new_node.data <= head.data:
        new_node.next = head
        head.prev = new_node
        return head

    cur = head
    prev = cur
    while cur is not None:
        if new_node.data <= cur.data:
            prev_temp = cur.prev
            prev_temp.next = new_node
            cur.prev = new_node
            new_node.prev = prev_temp
            new_node.next = cur
            break
        prev = cur
        cur = cur.next

    # if it is not added somewhere in the middle, it should go at the end
    new_node.prev = prev
    prev.next = new_node

    return head

n = Node(0)
print(SortedInsert(n, 2))
print(SortedInsert(n, 1))
print(SortedInsert(n, 4))
print(SortedInsert(n, 3))
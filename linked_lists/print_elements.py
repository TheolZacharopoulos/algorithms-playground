# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def print_list(head):
    cur = head
    while cur is not None:
        print(cur.data)
        cur = cur.next

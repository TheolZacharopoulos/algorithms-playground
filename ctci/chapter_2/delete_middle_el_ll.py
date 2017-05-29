"""
Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node.

EXAMPLE:
Input: the node ‘c’ from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a->b->d->e
"""

from ctci.chapter_2.LinkedList import LLNode, LinkedList


def delete_middle_element(elem):
    # This problem can not be solved if the node to be deleted
    # is the last node in the linked list.
    if elem is None or elem.next is None:
        return False

    next_elem = elem.next

    elem.data = next_elem.data
    elem.next = next_elem.next


if __name__ == '__main__':
    ll = LinkedList()

    ll.append('a')
    ll.append('b')
    ll.append('c')
    ll.append('d')
    ll.append('e')

    for e in ll:
        print(e.data, end=' ')

    print("\n=============")

    middle_element = ll.find_node('c')

    delete_middle_element(middle_element)

    for e in ll:
        print(e.data, end=' ')

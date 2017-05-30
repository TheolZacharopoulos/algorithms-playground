"""
Write a program to sort a stack in ascending order.
You should not make any assumptions about how the stack is implemented.
The following are the only functions that should be used to write this program:
push | pop | peek | isEmpty.
"""

from ctci.chapter_3.LLStack import Stack


def sort(stack):
    r = Stack()

    while not stack.is_empty():
        tmp = stack.pop()
        while not r.is_empty() and r.peek() > tmp:
            stack.push(r.pop())
        r.push(tmp)

    return r

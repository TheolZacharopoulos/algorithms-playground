from data_structures.stacks_queues.stacks.stack_ll import Stack

tokens = [
    ['(', ')'],
    ['[', ']'],
    ['{', '}']
]


def is_open_term(c):
    for bracket in tokens:
        if bracket[0] == c:
            return True
    return False


def matches(open, close):
    for bracket in tokens:
        if bracket[0] == open:
            return bracket[1] == close
    return False


def is_balanced(string):
    stack = Stack()

    for c in string:
        if is_open_term(c):
            stack.push(c)
        else:
            if not stack or not matches(stack.pop(), c):
                return False
    return True

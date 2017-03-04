# https://www.hackerrank.com/challenges/queue-using-two-stacks

# Logic :
# Always enqueue to enqueue_stack.
# Always dequeue from dequeue_stack (point 3 if empty).
# Transfer all elements from enqueue_stack to dequeue_stack if dequeue_stack is empty (if need to dequeue).

dequeue_stack, enqueue_stack = [], []

for _ in range(int(input())):
    val = list(map(int, input().split()))

    first = None

    if val[0] == 1:
        # if it is the first enqueue, keep the first value
        if len(enqueue_stack) == 0:
            first = val[1]

        # push the value
        enqueue_stack.append(val[1])

    elif val[0] == 2:
        if len(dequeue_stack) == 0:
            while len(enqueue_stack) > 0:
                dequeue_stack.append(enqueue_stack.pop())
        dequeue_stack.pop()

    else:
        if len(dequeue_stack) > 0:
            print(dequeue_stack[-1])
        else:
            print(first)

"""
Describe how you could use a single array to implement three stacks.
"""

"""
Approach 1:
Divide the array in three equal parts and allow the individual stack to grow in that limited space
» for stack 1, we will use [0, n/3)
» for stack 2, we will use [n/3, 2n/3)
» for stack 3, we will use [2n/3, n)
This solution is based on the assumption that we do not have any extra information
about the usage of space by individual stacks and that we can’t either modify or use any extra space.
With these constraints, we are left with no other choice but to divide equally.
"""


def approach_1(stack_size, number_of_arrays):
    arr = [0] * (stack_size * number_of_arrays)

    stack_pointers = [0] * number_of_arrays

    def push(stack_num, item):
        # Find the index of the top element in the array + 1, and * increment the stack pointer
        index = stack_num * stack_size + stack_pointers[stack_num] + 1
        stack_pointers[stack_num] += 1

        arr[index] = item

    def pop(stack_num):
        index = stack_num * stack_size + stack_pointers[stack_num]
        stack_pointers[stack_num] -= 1

        item = arr[index]
        arr[index] = 0

        return item

    def is_empty(stack_num):
        return stack_pointers[stack_num] == stack_num * stack_size

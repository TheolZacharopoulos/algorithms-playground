"""
In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of
different sizes which can slide onto any tower.
The puzzle starts with disks sorted in ascending order of size from top to bottom
(e.g., each disk sits on top of an even larger one). You have the following constraints:

(A) Only one disk can be moved at a time.
(B) A disk is slid of the top of one rod onto the next rod.
(C) A disk can only be placed on top of a larger disk.

Write a program to move the disks from the first rod to the last using Stacks.
"""

from ctci.chapter_3.LLStack import Stack


class Tower:
    def __init__(self, index):
        self.disks = Stack()
        self.index = index

    def index(self):
        return self.index

    def add(self, disk):
        if len(self.disks) != 0 and self.disks.peek() <= disk:
            raise Exception("Error placing disk " + str(disk))
        else:
            self.disks.push(disk)

    def move_top_to(self, tower):
        top = self.disks.pop()
        tower.add(top)
        print("Move disk " + str(top) + " from " + str(self.index()) + " to " + str(tower.index()))

    def move_disks(self, n, destination, buffer):
        if n > 0:
            self.move_disks(n - 1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(n - 1, destination, self)


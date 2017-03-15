def hanoi(disk, source, dest, aux):
    if disk == 1:
        print("Move disk 1 from peg " + str(source) + " to peg " + str(dest))
        return

    hanoi(disk - 1, source, aux, dest)
    print("Move disk " + str(disk) + " from peg  " + str(source) + " to peg " + str(dest))
    hanoi(disk - 1, aux, dest, source)


"""
|     |     |
|     |     |
|     |     |
-------------
A     B     C
"""

hanoi(1, 'A', 'B', 'C')
print("================================")
hanoi(2, 'A', 'B', 'C')
# hanoi(3, 'A', 'B', 'C')

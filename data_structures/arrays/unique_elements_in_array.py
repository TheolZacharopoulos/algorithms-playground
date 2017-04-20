"""
This problem is concerned with deleting repeated elements from a sorted array.
For example, for the array (2,3,5,5,7,11,11,11,13), then after deletion,
the array is (2,3,5,7,11,13,0,0,0). After deleting repeated elements,
there are 6 valid entries.
There are no requirements as to the values stored beyond the last valid element.

Write a program which takes as input a sorted array and updates it so that all
duplicates have been removed and the remaining elements have been shifted left to
fill the emptied indices. Return the number of valid elements.
"""

# Uses O(n) extra space (the map)
def unique_elems_map(array):
    unique = {}

    for i in array:
        unique[i] = True

    return len(unique)


# The time complexity is O(n), and th espace complexity is O(1),
# since all that is needed is the two additional variables.
def unique_elems(array):
    if not array:
        return 0

    write_index = 1
    for i in range(1, len(array)):
        if not array[write_index - 1] == array[i]:
            array[write_index] == array[i]
            write_index += 1

    return write_index



if __name__ == '__main__':
    print(unique_elems_map([2,3,5,5,7,11,11,11,13]))
    print(unique_elems([2,3,5,5,7,11,11,11,13]))

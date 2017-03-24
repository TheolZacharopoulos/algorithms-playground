from data_structures.stacks_queues.queues.linked_queue import LinkedQueue

# Time complexity:
#  - n for each divide and concatenation
#  - n-1 in worst case (when the array is sorted) for divide on pivot

# Therefore: O(n^2) in worst case.
# Paradoxically, if we choose the pivot as the last element of the sequence, this worst-case behavior occurs
# for problem instances when sorting should be easy—if the sequence is already sorted.
# Solution: Pick a random pivot

# Best case:
# - L, E, G be almost similar size: then O(n log n)
# Similar to mergesort, however quicksort just compares and increments an index,
# while merge sort copies values around (aux and back).


def quick_sort(a_queue):
    # list is already sorted
    if len(a_queue) < 2:
        return

    # using first as arbitrary pivot
    pivot = a_queue.first()

    lower = LinkedQueue()
    eq = LinkedQueue()
    greater = LinkedQueue()

    # divide S into L, E, and G
    while not a_queue.is_empty():
        if a_queue.first() < pivot:
            lower.enqueue(a_queue.dequeue())
        elif pivot < a_queue.first():
            greater.enqueue(a_queue.dequeue())
        else:
            eq.enqueue(a_queue.dequeue())  # a_queue.first() must equal pivot

    # conquer
    quick_sort(lower)  # sort elements less than p
    quick_sort(greater)  # sort elements greater than p

    # concatenate results
    while not lower.is_empty():
        a_queue.enqueue(lower.dequeue())

    while not eq.is_empty():
        a_queue.enqueue(eq.dequeue())

    while not greater.is_empty():
        a_queue.enqueue(greater.dequeue())


if __name__ == "__main__":
    arr = LinkedQueue()
    arr.enqueue(5)
    arr.enqueue(3)
    arr.enqueue(1)
    arr.enqueue(6)
    arr.enqueue(4)

    print(arr)
    quick_sort(arr)
    print(arr)

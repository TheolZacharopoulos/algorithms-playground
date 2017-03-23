from queue import Queue


def merge(low, high, queue):
    """Merge two sorted queue instances into an empty queue"""

    while not low.empty() and not high.empty():
        if low.top() < high.top():
            queue.put(low.get())
        else:
            queue.put(high.get())

    # move remaining elements of low to queue
    while not low.empty():
        queue.put(low.get())

    # move remaining elements of low to queue
    while not high.empty():
        queue.put(high.get())


def merge_sort(S):
    """Sort the elements of queue S using the merge-sort algorithm."""
    n = len(S)

    # list already sorted
    if n < 2:
        return

    # divide
    low = Queue()
    high = Queue()

    # move the first n//2 elements to low
    while low.qsize() < n // 2:
        low.put(S.get())

    # move the rest to high
    while not S.empty():
        high.put(S.get())

    # conquer
    merge_sort(low)
    merge_sort(high)

    # merge sorted halves back into S
    merge(low, high, S)

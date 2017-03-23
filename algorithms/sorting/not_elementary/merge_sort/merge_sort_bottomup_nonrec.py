# Time complexity: O(N log N)
# A bit faster than recursive merge-sort in practice, as it avoids the extra overheads of
# recursive calls and temporary memory at each level.

# The main idea is to perform merge-sort bottom-up,
# performing the merges level by level going up the merge-sort tree.

# Given an input array of elements, we begin by merging every successive pair of elements
# into sorted runs of length two. We merge these runs into runs of length four,
# merge these new runs into runs of length eight, and so on, until the array is sorted.


import math


def merge(src, result, start, inc):
    """Merge src[start:start+inc] and src[start+inc:start+2 inc] into result."""
    # boundary for run 1
    end1 = start + inc

    # boundary for run 2
    end2 = min(start + 2 * inc, len(src))

    # index into run 1, run 2, result
    x, y, z = start, start + inc, start

    while x < end1 and y < end2:
        if src[x] < src[y]:
            # copy from run 1 and increment x
            result[z] = src[x]
            x += 1
        else:
            # copy from run 2 and increment y
            result[z] = src[y]
            y += 1
        z += 1

    if x < end1:
        # copy remainder of run 1 to output
        result[z:end2] = src[x:end1]
    elif y < end2:
        # copy remainder of run 2 to output
        result[z:end2] = src[y:end2]


def merge_sort(arr):
    n = len(arr)
    logn = math.ceil(math.log(n, 2))

    # make temporary storage for dest
    src, dest = arr, [None] * n

    # pass i creates all runs of length 2i
    for i in (2**k for k in range(logn)):

        # each pass merges two length i runs
        for j in range(0, n, 2*i):
            merge(src, dest, j, i)

        # reverse roles of lists
        src, dest = dest, src

    # additional copy to get results to arr
    if arr is not src:
        arr[0:n] = src[0:n]

    return arr

if __name__ == "__main__":
    a = [5, 4, 2, 1, 3, 8, 6]
    print(a)
    print(merge_sort(a))

# https://www.hackerrank.com/challenges/quicksort2

# The first element in a sub-array should be used as a pivot.
# Partition the left side before partitioning the right side.
# The pivot should be placed between sub-arrays while merging them.
# Array of length 1 or less will be considered sorted, and there is no need to sort or to print them.


def quick_sort(ar):
    if len(ar) < 2:
        return ar

    lt, eq, rt = [], [], []

    for item in ar:
        if item < ar[0]:
            lt.append(item)
        elif item > ar[0]:
            rt.append(item)
        else:
            eq.append(item)

    sub = quick_sort(lt) + eq + quick_sort(rt)

    print(' '.join(map(str, sub)))

    return sub

if __name__ == "__main__":
    a = [5, 8, 1, 3, 7, 9, 2]
    quick_sort(a)

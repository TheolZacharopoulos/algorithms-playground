# Given an array of N items, find the k'th largest
# Ex. Min (k=0), Max(k=N), median(k=N/2)

# Is selection as slow as sorting? (n*log n) or can it be done in linear time (n)
# Use quick sort:
# - entry a[j] is in place
# - No larger entry to the left of j
# - No smaller entry to the right of j

# Repeat in ONE subarray, depending on j; finished when j equals k.
# - if j == k: we are done
# - if j > k: we go to the left, set high to the j-1
# - if j < k: we go to the right, set low to the j+1


from random import shuffle


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(a, lo, hi):
    i = lo + 1
    j = hi

    while True:
        while a[i] < a[lo]:
            if i == hi:
                break
            i += 1

        while a[lo] < a[j]:
            if j == lo:
                break
            j -= 1

        if i >= j:
            break
        swap(a, i, j)
    swap(a, lo, j)
    return j


def select(array, k):
    shuffle(array)

    low = 0
    high = len(array) - 1

    while low < high:
        j = partition(array, low, high)

        if j < k:
            low = j + 1
        elif j > k:
            high = j - 1
        else:
            return array[k]
    return array[k]


if __name__ == "__main__":
    arr = [5, 4, 1, 2, 7, 6, 8, 9, 10, 3]
    print(select(arr, 9))

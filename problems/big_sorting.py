#!/bin/python

import sys

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)


# your code goes here
def radix_sort(to_sort):
    radix = 5
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        # declare and initialize buckets
        buckets = [list() for _ in range(radix)]

        # split to_sort between lists
        for i in to_sort:
            tmp = i / placement
            buckets[int(tmp % radix)].append(i)
            if max_length and tmp > 0:
                max_length = False

        # empty lists into to_sort array
        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                to_sort[a] = i
                a += 1

        # move to next digit
        placement *= radix
    return to_sort


unsorted = map(int, unsorted)

for e in radix_sort(unsorted):
    print(e)
"""
Write a method that returns all subsets of a set.

https://www.youtube.com/watch?v=L3VZjFSbCWI

SUBSETS:
2^n possible subsets

1: [[], [1]]
2: [[], [1], [2], [1, 2]]
3: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
4: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [3, 4], [1, 2, 3, 4]]

"""


def subsets_of(s):
    subsets = []

    # empty set
    subsets.append([])

    for i in s:
        for j in range(0, len(subsets)):
            temp = list(subsets[j])  # list() in order to copy it
            temp.append(i)

            subsets.append(temp)

    return subsets


if __name__ == '__main__':
    s = {1, 2, 3, 4}

    print(subsets_of(s))

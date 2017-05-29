"""
Implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures?

Solutions:
    1. Brute force:
    Check every char of the string with every other char of the string for duplicate occurrences.
    This will take O(n^2) time and no space.

    2. Sorting:
    If we are allowed to destroy the input string, we could sort the string in O(n log n) time
    and then linearly check the string for neighboring characters that are identical.

    3:
"""


def is_unique(string):
    """
    For simplicity, assume char set is ASCII (if not, we need to increase the storage size. The rest
    of the logic would be the same). NOTE: This is a great thing to point out to your interviewer!
    """

    char_set = [False] * 256

    for c in string:
        index = ord(c) - ord('A')

        if char_set[index] is True:
            return False

        char_set[index] = True

    return True


if __name__ == '__main__':
    s1 = "Hello"
    s2 = "HeLlO"
    s3 = "world"

    assert not is_unique(s1)
    assert is_unique(s2)
    assert is_unique(s3)


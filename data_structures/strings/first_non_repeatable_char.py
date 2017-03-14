# Write an efficient function to find the first nonrepeated character in a string.
# For instance, the first nonrepeated character in “total” is 'o' and the first nonrepeated character in “teeter” is 'r'.
# Discuss the efficiency of your algorithm.

from enum import Enum


class Seen(Enum):
    SEEN = 0
    SEEN_MULTIPLE = 1


def remove_first_rep(string):
    seen_map = {}

    for c in string:
        seen_map[c] = None

    for c in string:
        if seen_map[c] is None:
            seen_map[c] = Seen.SEEN
        else:
            seen_map[c] = Seen.SEEN_MULTIPLE

    for c in string:
        if seen_map[c] == Seen.SEEN:
            return c

    return None

print(remove_first_rep("total"))
print(remove_first_rep("teeter"))

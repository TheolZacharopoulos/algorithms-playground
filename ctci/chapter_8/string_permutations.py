"""
Write a method to compute all permutations of a string

Solution:
Let’s assume a given string S represented by the letters A1, A2, A3, ..., An
To permute set S, we can select the first character, A1, permute the remainder of the string to get a new list.
Then, with that new list, we can “push” A1 into each possible position.

For example, if our string is “abc”, we would do the following:
1. Let first = “a” and let remainder = “bc”
2. Let list = permute(bc) = {“bc”, “cd”}
3. Push “a” into each location of “bc” (--> “abc”, “bac”, “bca”) and “cb” (--> “acb”, “cab”, “cba”)
4. Return our new list
"""


def get_perms(s):
    if s is None:
        return None

    perms = []

    # base case
    if len(s) == 0:
        perms.append("")
        return perms

    first = s[0]
    remainder = s[1:]

    words = get_perms(remainder)

    for word in words:
        for i in range(0, len(word)+1):
            perms.append(insert_char_at(word, first, i))

    return perms


def insert_char_at(word, c, i):
    return word[0:i] + c + word[i:]


if __name__ == '__main__':
    string = "abc"
    print(get_perms(string))

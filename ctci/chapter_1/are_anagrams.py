"""
Write a method to decide if two strings are anagrams or not.
"""


def are_strings_anagrams_with_sort(str1, str2):
    return sorted(str1) == sorted(str2)


def get_char_count_array(string):
    a = [0] * 256

    for c in string:
        a[ord(c) - ord('a')] += 1

    return a


def are_strings_anagrams(str1, str2):
    """
    Check if the two strings have identical counts for each unique char.
    """

    a1 = get_char_count_array(str1)
    a2 = get_char_count_array(str2)

    for c in str1:
        if a1[ord(c) - ord('a')] != a2[ord(c) - ord('a')]:
            return False

    return True


if __name__ == '__main__':
    print(are_strings_anagrams("abc", "dfg"))
    print(are_strings_anagrams("abc", "cab"))

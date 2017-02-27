# https://www.hackerrank.com/challenges/ctci-making-anagrams


def number_needed(a, b):
    char_arr = [0] * 26

    for c in a:
        char_arr[ord(c) - ord('a')] += 1

    for c in b:
        char_arr[ord(c) - ord('a')] -= 1

    sum_chars = 0
    for x in char_arr:
        sum_chars += abs(x)

    return sum_chars


a = input().strip()
b = input().strip()

print(number_needed(a, b))

# https://www.hackerrank.com/challenges/two-characters

from itertools import combinations


def meet_pattern(s):
    return all(s[i-1] != s[i] for i in range(1, len(s)))

s_len = int(input().strip())
s = input().strip()
letters = set(s)
max_len = 0

for pair in combinations(letters, 2):
    substr = "".join(i for i in s if i in pair)

    if meet_pattern(substr):
        max_len = max(max_len, len(substr))

print(max_len)

# https://www.hackerrank.com/challenges/funny-string


def funny_string(string):
    s = list(string)
    r = s[::-1]

    for i in range(1, len(s)):
        for j in range(len(r)-1, -1, -1):
            if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
                return "Not Funny"

    return "Funny"

print(funny_string("acxz"))
print(funny_string("bcxz"))

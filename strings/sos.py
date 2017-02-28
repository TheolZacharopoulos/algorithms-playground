# https://www.hackerrank.com/challenges/mars-exploration


def count_sos(string):
    sos_num = 0

    i = 1
    s = list(string)

    while i < len(s):
        if s[i-1] != 'S':
            sos_num += 1

        if s[i] != 'O':
            sos_num += 1

        if s[i + 1] != 'S':
            sos_num += 1

        i += 3

    return sos_num

print(count_sos("SOSSPSSQSSOR"))
print(count_sos("SOSSOT"))

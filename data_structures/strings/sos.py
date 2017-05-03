# https://www.hackerrank.com/challenges/mars-exploration


def count_sos(string):
    sos_num = 0

    s = list(string)

    for i in range(1, len(s), 3):
        if s[i-1] != 'S':
            sos_num += 1

        if s[i] != 'O':
            sos_num += 1

        if s[i + 1] != 'S':
            sos_num += 1

    return sos_num

print(count_sos("SOSSPSSQSSOR"))
print(count_sos("SOSSOT"))

# https://www.hackerrank.com/challenges/camelcase


def camel_case_worlds_num(string):
    if len(string) == 0:
        return 0

    words = 1
    for c in list(string):
        if c.isupper():
            words += 1

    return words

print(camel_case_worlds_num("saveChangesInTheEditor"))

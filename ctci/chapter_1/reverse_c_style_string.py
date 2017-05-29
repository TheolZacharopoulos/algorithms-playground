"""
Write code to reverse a C-Style String.
(C-String means that "abcd" is represented as  ve characters, including the null character.)
"""


def reverse_string(string):
    end = string
    end_i = 0
    string_i = 0

    while end[end_i] is not None:
        end_i += 1

    end_i -= 1

    while string_i < end_i:
        tmp = string[string_i]

        string[string_i] = end[end_i]
        string_i += 1

        end[end_i] = tmp
        end_i -= 1

if __name__ == '__main__':
    string1 = ['a', 'b', 'c', 'd', 'e', None]
    reverse_string(string1)
    print(string1)

    string2 = ['a', 'b', 'c', 'd', None]
    reverse_string(string2)
    print(string2)

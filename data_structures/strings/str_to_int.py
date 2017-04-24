# Converts a string to a signed integer. You may assume that the string contains only digits
# and the minus character ('-'), that it is a properly formatted integer number,
# and that the number is within the range of an int type.
# And the other way around.


def str_to_int(string):
    number = 0
    i = 0
    is_negative = False

    string_arr = list(string)

    if string_arr[0] == '-':
        is_negative = True
        i = 1

    while i < len(string_arr):
        number *= 10
        number += (ord(string_arr[i]) - ord('0'))
        i += 1

    if is_negative:
        number = -number

    return number


def int_to_str(num):
    string = ""
    is_negative = False

    if num < 0:
        is_negative = True

    string += str(abs(num) % 10)
    num = int(abs(num) / 10)

    while num != 0:
        string += str(abs(num) % 10)
        num = int(abs(num) / 10)

    if is_negative:
        string += '-'

    return string[::-1]


assert str_to_int("0") == 0
assert str_to_int("1") == 1
assert str_to_int("-1") == -1
assert str_to_int("123") == 123
assert str_to_int("-123") == -123

assert int_to_str(1) == "1"
assert int_to_str(-1) == "-1"
assert int_to_str(123) == "123"
assert int_to_str(-123) == "-123"

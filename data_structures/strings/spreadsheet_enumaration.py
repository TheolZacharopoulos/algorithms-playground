"""
Spreadsheets often use an alphabetical encoding of the successive columns.
Specifically, columns are identified by "A", "B", "C", ..., "X", "Y", "Z", "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
Implement a function that converts a spreadsheet column id to the corresponding integer,
with "A" corresponding to 1.
For example, you should return 4 for "D", 27 for "AA", 702 for "ZZ", etc. How would you test your code?

Solution:
This problem is basically the problem of converting a string representing a base-26 number to the corresponding integer,
except that "A" corresponds to 1 not 0.
For example to convert "ZZ", we initialize result to 0.
We add 26, multiply by 26, then add 26 again, i.e., the id is 262 + 26 = 702.
"""


def ss_decode_col_id(col):
    result = 0

    for i in range(len(col)):
        c = col[i]
        result = result * 26 + ord(c) - ord('A') + 1
    return result


if __name__ == '__main__':
    print(ss_decode_col_id("D"))
    print(ss_decode_col_id("AA"))
    print(ss_decode_col_id("ZZ"))

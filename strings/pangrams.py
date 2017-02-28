# https://www.hackerrank.com/challenges/pangrams


def is_pangram(string):
    char_map = {}

    string_arr = list(string)

    for c in string_arr:
        # skip spaces
        if c != ' ':
            char_map[c.lower()] = True

    # includes all the 26 characters
    if len(char_map) == 26:
        print("pangram")
    else:
        print("nnot pangram")


is_pangram("We promptly judged antique ivory buckles for the next prize")
is_pangram("We promptly judged antique ivory buckles for the prize")
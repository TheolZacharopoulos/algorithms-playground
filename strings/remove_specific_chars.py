# Write an efficient function that deletes characters from an ASCII string.
# Use the prototype `string removeChars( string str, string remove );`
# where any character existing in remove must be deleted from str.
# For example, given a str of "Battle of the Vowels: Hawaii vs. Grozny" and a remove of "aeiou",
# the function should transform str to “Bttl f th Vwls: Hw vs. Grzny”.
# Justify any design decisions you make, and discuss the efficiency of your solution.


def remove_chars(string, remove):
    to_remove = {}

    for s in string:
        to_remove[s] = False

    for r in remove:
        to_remove[r] = True

    dest_string = []
    for src in range(0, len(string)):
        char = string[src]
        if to_remove[char] is False:
            dest_string.append(char)

        # if it was another language:
        # dest_string[dest++] = char

    # char array to string
    return ''.join(dest_string)

print(remove_chars("Battle of the Vowels: Hawaii vs. Grozny", "aeiou"))

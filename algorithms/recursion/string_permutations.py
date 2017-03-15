# Implement a routine that prints all possible orderings of the characters in a string.
# In other words, print all permutations that use all the characters from the original string.
#
# For example, given the string “hat”, your function should print the strings
# “tha”, “aht”, “tah”, “ath”, “hta”, and “hat”.
#
# Treat each character in the input string as a distinct character,
# even if it is repeated. Given the string “aaa”, your routine should print “aaa” six times.
# You may print the permutations in any order you choose.


# To find all permutations starting at position n, successively place all allowable letters in position n,
# and for each new letter in position n find all permutations starting at position n + 1 (the recursive case).
# When n is greater than the number of characters in the input string,
# a permutation has been completed; print it and return to changing letters at positions less than n (the base case).
#
# “all allowable letters” means all letters in the input string that haven’t already been chosen for a position
# to the left of the current position.
# You can eliminate these inefficient scans by maintaining an array of boolean values corresponding to the positions
# of the letters in the input string and using this array to mark letters as used or unused, as appropriate.


class Permutations:
    def __init__(self, in_string):
        # The string to permute
        self.in_string = in_string

        # Keeps the allowable letters, which letter can be used in a permutation
        self.used = [False] * len(self.in_string)

        self.out_string = ""

    def permute(self):

        # A permutation is found
        if len(self.in_string) == len(self.out_string):
            print(self.out_string)
            return

        # for each character in the input string
        for i in range(len(self.in_string)):

            # in case it the letter has been used, skip to the next (No duplicates)
            if self.used[i] is True:
                continue

            # Add letter to the output string
            self.out_string += self.in_string[i]

            self.used[i] = True
            self.permute()
            self.used[i] = False

            self.out_string = self.out_string[0:-1]

p = Permutations("abcd")
p.permute()

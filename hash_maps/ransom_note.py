# https://www.hackerrank.com/challenges/ctci-ransom-note

# A kidnapper wrote a ransom note but is worried it will be traced back to him.
# He found a magazine and wants to know if he can cut out whole words from it and use them to create
# an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words
# available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

# Given the words in the magazine and the words in the ransom note,
# print Yes if he can replicate his ransom note exactly using whole words from the magazine;
# otherwise, print No.


def ransom_note(mag, note):
    freq = {}

    for mag_word in mag:
        freq[mag_word] = 1 + freq.get(mag_word, 0)

    for note_word in note:
        if freq.get(note_word, 0) < 1:
            return False
        else:
            freq[note_word] = freq.get(note_word) - 1

    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')

answer = ransom_note(magazine, ransom)

if answer:
    print("Yes")
else:
    print("No")

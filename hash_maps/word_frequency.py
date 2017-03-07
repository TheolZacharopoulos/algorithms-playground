# Consider the problem of counting the number of occurrences of words in a document.


def count_words(filename):
    freq = {}

    for piece in open(filename).read().lower().split():
        # only consider alphabetic characters within this piece
        word = ''.join(c for c in piece if c.isalpha())

        # require at least one alphabetic character
        if word:
            freq[word] = 1 + freq.get(word, 0)

    max_word = ''
    max_freq = 0

    for (word, count) in freq.items():
        if count > max_freq:
            max_freq = count
            max_word = word

    return max_word, max_freq

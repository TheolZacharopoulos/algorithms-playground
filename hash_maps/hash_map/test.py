from hash_maps.hash_map.ChainHashMap import ChainHashMap
from hash_maps.hash_map.ProbeHashMap import ProbeHashMap


def count_words(text, freq):
    for piece in text.lower().split():
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


w_chain, f_chain = count_words(
    "The tyranny is ostensibly overseen by Big Brother, the Party leader who enjoys an intense cult of personality, "
    "but who may not even exist. The Party seeks power entirely for its own sake. "
    "It is not interested in the good of others; it is interested solely in power.",
    ChainHashMap())


print(w_chain)

w_probe, f_probe = count_words(
    "The tyranny is ostensibly overseen by Big Brother, the Party leader who enjoys an intense cult of personality, "
    "but who may not even exist. The Party seeks power entirely for its own sake. "
    "It is not interested in the good of others; it is interested solely in power.",
    ProbeHashMap())

print(w_probe)

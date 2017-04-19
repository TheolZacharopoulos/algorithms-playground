"""
It consists of two nested loops, with the outer loop indexing through
all possible starting indices of the pattern in the text,
and the inner loop indexing through each character of the pattern,
comparing it to its potentially corresponding character in the text.

The worst-case running time of the brute-force method is O(nm).
"""


def find_brute(pat, txt):
    """Return the lowest index of txt at which substring pattern begins (or else -1)."""
    M = len(pat)
    N = len(txt)

    for i in range(N - M + 1):  # try every potential starting index within text

        k = 0  # an index into pattern
        while k < M and txt[i + k] == pat[k]:  # kth character of pattern matches
            k += 1
            
        if k == M:  # if we reached the end of pattern,
            return i  # substring txt[i:i+m] matches pattern

    return -1  # failed to find a match starting with any i

# Write a function that reverses the order of the words in a string.
# For example, your function should transform the string "Do or do not, there is no try." to
# "try. no is there not, do or Do". Assume that all words are space delimited and treat punctuation the same as letters.


def reverse_words(string):
    start = 0
    end = 0
    length = len(string)

    # Reverse the entire string
    string_arr = list(string)
    reverse_word(string_arr, start, length - 1)

    while end < length:
        # skip non-word characters
        if string_arr[end] != ' ':

            # save the position of beginning of word
            start = end

            # scan to the next non-word character
            while end < length and string_arr[end] != ' ':
                end += 1

            # back to the end of the word
            end -= 1

            # reverse the word
            reverse_word(string_arr, start, end)

        end += 1

    return ''.join(string_arr)


def reverse_word(word_arr, start, end):
    while start < end:
        temp = word_arr[start]
        word_arr[start] = word_arr[end]
        word_arr[end] = temp
        start += 1
        end -= 1

    return word_arr


print(reverse_words("Do or do not, there is no try."))

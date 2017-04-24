def is_anagram(word):
    j = len(word) - 1
    i = 0

    while i <= j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    print(is_anagram("hello"))
    print(is_anagram("anna"))

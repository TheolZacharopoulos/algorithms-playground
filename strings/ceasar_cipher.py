# http://www.hackerrank.com/challenges/caesar-cipher-1


def ceasar(string, key):
    string_arr = list(string)

    for i in range(len(string_arr)):
        c = string_arr[i]

        # The cipher only encrypts letters
        if c.isalpha():
            # calculate new character (keep it in range)
            a = 'A' if c.isupper() else 'a'
            string_arr[i] = chr(ord(a) + (ord(c) - ord(a) + key) % 26)
        else:
            string_arr[i] = c

    return ''.join(string_arr)


print(ceasar("middle-Outz", 2))
print(ceasar("Hello_World!", 4))

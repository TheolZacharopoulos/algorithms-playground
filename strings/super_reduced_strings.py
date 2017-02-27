# https://www.hackerrank.com/challenges/reduced-string


def reduced_strings(string):
    arr = list(string)
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            del arr[i]
            del arr[i]

            i = 0
            if len(arr) == 0:
                return "Empty String"
        else:
            i += 1

    return ''.join(arr)


print(reduced_strings("aaabcddd"))
print(reduced_strings("baab"))
print(reduced_strings("aa"))

# https://www.hackerrank.com/challenges/sparse-arrays

N = int(input().strip())

strings = {}

# Put the values in a map with their frequencies
for _ in range(N):
    string = input().strip()
    if string in strings:
        cnt = strings.get(string)
        strings[string] = cnt + 1
    else:
        strings[string] = 1

Q = int(input().strip())

# Use the frequencies for each query
for _ in range(Q):
    q = input().strip()
    if q in strings:
        print(strings[q])
    else:
        print(0)

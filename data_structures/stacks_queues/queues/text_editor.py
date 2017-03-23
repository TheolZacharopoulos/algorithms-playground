# https://www.hackerrank.com/challenges/simple-text-editor


n = int(input())

string = ""
history = []

for i in range(n):
    inp = input().strip().split(' ')

    if inp[0] == '1':
        history.append(string)
        string = string + inp[1]

    elif inp[0] == '2':
        history.append(string)
        deletion = int(inp[1])
        pos = len(string) - deletion
        string = string[0:pos]

    elif inp[0] == '3':
        pos = int(inp[1]) - 1
        print(string[pos])

    else:
        string = history.pop()

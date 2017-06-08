"""
https://www.hackerrank.com/challenges/game-of-two-stacks
"""

g = int(input().strip())

for a0 in range(g):
    n, m, x = input().strip().split(' ')
    n, m, x = [int(n), int(m), int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    # your code goes here
    s = 0
    count = 0
    i = 0
    while s <= x:
        m = 0
        if len(a) > 0 and len(b) > 0:
            if a[0] < b[0]:
                m = a.pop(0)
            else:
                m = b.pop(0)
        elif len(a) > 0:
            m = a.pop(0)
        elif len(b) > 0:
            m = b.pop(0)
        else:
            count += 1
            break

        s += m
        count += 1
    print(count - 1)

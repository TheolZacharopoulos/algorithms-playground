coins = [1, 3]
S = 5


def find_coins_num(v, s):
    m = [float('inf') for _ in range(s + 1)]
    m[0] = 0

    for i in range(1, s + 1):
        for j in (0, len(v) - 1):
            if v[j] <= i and m[i - v[j]] + 1 < m[i]:
                m[i] = m[i - v[j]] + 1

    return m[s]

print(find_coins_num(coins, S))

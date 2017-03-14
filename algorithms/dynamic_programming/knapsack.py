class Item:
    def __init__(self, weight, value, freq=1):
        self.weight = weight
        self.value = value
        self.freq = freq


def knapsack_rep(items, W):
    N = len(items)
    K = [0 for _ in range(W + 1)]

    # we dont really need this since it is initialised
    K[0] = 0
    for w in range(1, W + 1):
        maxim = float('-inf')
        for i in range(0, N):
            if items[i].weight <= w:
                val = (K[w - items[i].weight] + items[i].value)
                if maxim < val:
                    maxim = val
            K[w] = maxim

    print(K)

    return K[W]


def knapsack_no_rep(items, W):
    N = len(items)
    K = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    # we dont really need this since it is initialised
    for i in range(N + 1):
        K[i][0] = 0
    for j in range(W + 1):
        K[0][j] = 0

    for j in range(1, N+1):
        for w in range(1, W+1):
            if items[j].weight > w:
                K[w][j] = K[w][j - 1]
            else:
                K[w][j] = max(K[w][j - 1], K[w - items[j].weight][j - 1] + items[j].value)

    return K[W][N]

theItems = [
    Item(6, 30),
    Item(3, 14),
    Item(4, 16),
    Item(2, 9)
]

print(knapsack_rep(theItems, 10))
# print(knapsack_no_rep(theItems, 10))

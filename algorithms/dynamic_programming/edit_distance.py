def find_edit_distance(x, y):
    E = [[10 for _ in range(len(y))] for _ in range(len(x))]

    def diff(x_i, y_i):
        if x[x_i] == y[y_i]:
            return 0
        else:
            return 1

    for i in range(len(x)):
        E[i][0] = i

    for j in range(len(y)):
        E[0][j] = j

    for i in range(1, len(x)):
        for j in range(1, len(y)):
            E[i][j] = min(
                E[i - 1][j] + 1,
                E[i][j - 1] + 1,
                E[i - 1][j - 1] + diff(i, j))

    return E[len(x)-1][len(y)-1]


print(find_edit_distance("EXPONENTIAL", "POLYNOMIAL"))

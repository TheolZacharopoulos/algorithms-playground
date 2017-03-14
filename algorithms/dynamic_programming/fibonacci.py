def fib_rec(x):
    if x <= 1:
        return x
    else:
        return fib_rec(x-1) + fib_rec(x-2)


def fib_dp(x):
    if x <= 1:
        return x
    else:
        f = [0 for _ in range(x+1)]
        f[0] = 0
        f[1] = 1

        for i in range(2, x+1):
            f[i] = f[i - 1] + f[i - 2]

        return f[x]

print(fib_dp(10))
print(fib_rec(10))

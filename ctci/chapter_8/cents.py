"""
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent),
write code to calculate the number of ways of representing n cents.
"""


def make_change(n, denom):
    next_denom = 0

    if denom == 25:
        next_denom = 10
    elif denom == 10:
        next_denom = 5
    elif denom == 5:
        next_denom = 1
    elif denom == 1:
        return 1

    ways = 0

    i = 0
    while (i * denom) <= n:
        ways += make_change(n - i * denom, next_denom)
        i += 1

    return ways


if __name__ == '__main__':
    print(make_change(10, 25))

# https://www.hackerrank.com/challenges/ctci-recursive-staircase
# Davis has S staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time.
# Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.

# Given the respective heights for each of the  staircases in his house,
# find and print the number of ways he can climb each staircase on a new line.


# multi-recursive O(3^n) time
def davis_staircase_rec(steps):
    if steps < 0:
        return 0
    if steps == 0:
        return 1

    return davis_staircase_rec(steps - 1) + davis_staircase_rec(steps - 2) + davis_staircase_rec(steps - 3)


# Memoization O(n) time, but O(n) memory space
def davis_staircase_memo(steps):
    def davis_staircase_memo_real(st, memo):
        if st < 0:
            return 0
        if st == 0:
            return 1

        if memo[st] == 0:
            memo[st] = \
                davis_staircase_memo_real(st - 1, memo) + \
                davis_staircase_memo_real(st - 2, memo) + \
                davis_staircase_memo_real(st - 3, memo)

        return memo[st]

    return davis_staircase_memo_real(steps, [0 for _ in range(steps + 1)])


# Dynamic programming approach O(n) time, memory space O(n)
def davis_staircase_dp(steps):
    if steps < 0:
        return 0
    if steps <= 1:
        return 1

    paths = [0 for _ in range(steps + 1)]
    paths[0] = 1
    paths[1] = 1
    paths[2] = 2

    for i in range(3, steps + 1):
        paths[i] = paths[i - 1] + paths[i - 2] + paths[i - 3]

    return paths[steps]


# Iterative version, O(n) time, O(1) memory space, we do not really need the memo table (we only need 3 values)
def davis_staircase_iterative(steps):
    if steps < 0:
        return 0
    if steps <= 1:
        return 1

    # the initial array
    paths = [1, 1, 2]

    # the last value is just the sum of the previous 3 values
    for i in range(3, steps + 1):
        count = paths[2] + paths[1] + paths[0]

        # swift the values
        paths[0] = paths[1]
        paths[1] = paths[2]
        paths[2] = count

    return paths[2]


# there is only one way for him to climb it (1)
print(davis_staircase_rec(1) ==
      davis_staircase_memo(1) ==
      davis_staircase_dp(1) ==
      davis_staircase_iterative(1))

# 1-1-1, 2-1, 1-2, 3 (4)
print(davis_staircase_rec(3) ==
      davis_staircase_memo(3) ==
      davis_staircase_dp(3) ==
      davis_staircase_iterative(3))

# .... (44)
print(davis_staircase_rec(7) ==
      davis_staircase_memo(7) ==
      davis_staircase_dp(7) ==
      davis_staircase_iterative(7))

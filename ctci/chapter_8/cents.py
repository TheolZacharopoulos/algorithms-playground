"""
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent),
write code to calculate the number of ways of representing n cents.

e.g.

make_change(27, [25, 10, 5, 1])
 0 quarter -> make_change(27, [10, 5, 1])
              0 dimes -> make_change(27, [5, 1])
                         0 nickles -> make_change(27, [1])

                         1 nickles -> make_change(22, [1])
                         3 nickles -> make_change(12, [1])
                         4 nickles -> make_change(7,  [1])
                         5 nickles -> make_change(2,  [1])
                            ....
                            make_change(17,  [1]) = 1 (Base case)
                            make_change(17,  [2]) = 1 (Base case)

              1 dimes -> make_change(17, [5, 1])
              2 dimes -> make_change(7,  [5, 1])
 1 quarter -> make_change(2, [10, 5, 1])

"""


def make_change(money, coins, index=0):
    # Base case,
    # no matter what the coin is there is only 1 way to get 0 money
    if money == 0:
        return 1

    # Base case,
    # We run out of coins
    if index >= len(coins):
        return 0

    amount_with_coin = 0
    num_of_ways = 0
    while amount_with_coin <= money:
        remaining = money - amount_with_coin
        num_of_ways += make_change(remaining, coins, index + 1)
        amount_with_coin += coins[index]

    return num_of_ways


# we need a key that defines bot the money and the index
def make_change_DP(money, coins, index=0, memo={}):
    # Base case,
    # no matter what the coin is there is only 1 way to get 0 money
    if money == 0:
        return 1

    # Base case,
    # We run out of coins
    if index >= len(coins):
        return 0

    key = str(money) + '-' + str(index)  # use separator otherwise: "22" + "1" == "2" + "21"

    if key in memo:
        return memo[key]

    amount_with_coin = 0
    num_of_ways = 0
    while amount_with_coin <= money:
        remaining = money - amount_with_coin
        num_of_ways += make_change_DP(remaining, coins, index + 1, memo)
        amount_with_coin += coins[index]

    memo[key] = num_of_ways

    return num_of_ways

if __name__ == '__main__':
    print(make_change(50, [25, 10, 5, 1]))
    print(make_change_DP(50, [25, 10, 5, 1]))


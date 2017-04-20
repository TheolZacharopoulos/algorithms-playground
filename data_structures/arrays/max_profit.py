def compute_max_profit(prices):
    min_price = float('inf')
    max_profit = 0.0

    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


if __name__ == '__main__':
    print(compute_max_profit([310,315,275,295,260,270,290,230,255,250]))

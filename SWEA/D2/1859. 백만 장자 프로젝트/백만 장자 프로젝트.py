T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    prices = [int(x) for x in input().split()]
    max_price, profit = 0, 0
    for price in prices[::-1]:
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price

    print(f"#{test_case} {profit}")
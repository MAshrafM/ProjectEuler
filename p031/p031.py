def p031():
    print("Coin sums")
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = []

    for i in range(0, 201):
        ways.append(0)
    ways[0] = 1


    for coin in coins:
        for i in range(coin, target+1):
            ways[i] += ways[i-coin]

    return(f"p031 Ans: {ways[target]}")
#Task 3.1
def gready_coin(N, coins):
    coins.sort(reverse=True)
    total_coins = 0
    result = []
    total_amount = 0
    for coin in coins:
        if N >= coin:
            count = N // coin
            total_coins += count
            total_amount += count
            for i in range(total_coins):
                result.append(coin)
            N -= count * coin
        total_coins = 0
    return f"Coins: {result}, total of {total_amount}"


coins = [1, 5, 11]

print(gready_coin(15, coins))


 #Task 3.2 
def optimize_gready_coin(N,coins):
    coins.sort(reverse=True)
    results = [float("inf")] * (N+1)
    results[0] = 0
    coinsss = {}
    
    for i in range(1, N+1):
        for coin in coins:
            if coin <= i:
                q = min(results[i], results[i - coin]+1)
                coinsss[q] = str(coin)
                print(coinsss)
                results[i] = q
    return results[N]

coins = [1,5,11]
print("VÅR")
print(optimize_gready_coin(15, coins))
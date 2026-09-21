## G5 2294 동전2
import sys
ip = sys.stdin.readline

## 입력
n, k = map(int, ip().split())

coins = set()
for _ in range(n): coins.add(int(ip()))
coins = sorted(list(coins))
n = len(coins)

## DP
DP = [[0] * (n+1) for _ in range(k+1)]

for dp_index in range(0, k+1):
    min_count = 100000
    min_index = -1
    min_coin = -1

    for coin_index in range(n):
        hist = dp_index - coins[coin_index]
    
        if hist == 0: 
            DP[dp_index][coin_index] = 1
            DP[dp_index][n] = 1
            min_index = -1

        elif (hist > 0) and DP[hist][n] > 0:
            if DP[hist][n] < min_count:
                min_count = DP[hist][n]
                min_index = hist
                min_coin = coin_index

    if min_index > -1:
        for coin_index in range(n):
            DP[dp_index][coin_index] = DP[min_index][coin_index]
            if coin_index == min_coin:
                DP[dp_index][coin_index] = DP[min_index][coin_index] + 1
        DP[dp_index][n] = DP[min_index][n] + 1


if DP[k][n]: print(DP[k][n])
else       : print(-1)
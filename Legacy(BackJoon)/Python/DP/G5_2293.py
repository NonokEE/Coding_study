## G5 2293 동전 1
import sys
ip = sys.stdin.readline

## 입력
n, k = map(int, ip().split())
coins = []
for _ in range(n): coins.append(int(ip()))
coins.sort()

## DP
DP = [0] * (k+1)
DP[0] = 1
for c in coins:
    for i in range(c, k+1):
        DP[i] += DP[i-c]

print(DP[k])
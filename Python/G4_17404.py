## G4 17404 RGB거리 2
import sys
ip = sys.stdin.readline

## 입력
N = int(ip())

costs = []
for _ in range(N): costs.append(list(map(int, ip().split())))

## DP
res = sys.maxsize

for first_house in range(3):
    dp = [[sys.maxsize]*3 for _ in range(N)]
    dp[0][first_house] = costs[0][first_house]

    for house_index in range(1, N):
        dp[house_index][0] = costs[house_index][0] + min(dp[house_index-1][1], dp[house_index-1][2])
        dp[house_index][1] = costs[house_index][1] + min(dp[house_index-1][0], dp[house_index-1][2])
        dp[house_index][2] = costs[house_index][2] + min(dp[house_index-1][0], dp[house_index-1][1])

    for last_house in range(3):
        if first_house != last_house: res = min(res, dp[-1][last_house])

print(res)


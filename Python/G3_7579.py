## G3 7579 앱
import sys
ip = sys.stdin.readline

## 입력
N, M = map(int, ip().split())
ms = list(map(int, ip().split()))
cs = list(map(int, ip().split()))

## 전처리
temp_ms = [0]
temp_cs = [0]

for i in range(N):
    if cs[i]: ## 코스트가 1이상인 경우에만 새 테이블에 등록
        temp_ms.append(ms[i])
        temp_cs.append(cs[i])
    else: ##코스트가 0이면 테이블에 등록 안하고 바로 M에 감산해줘도 된다.
        M -= ms[i]

if M <= 0:
    print(0)
    quit()

ms = temp_ms
cs = temp_cs

## 알고리즘 수행 (DP)
dp = [[0] * (sum(cs)+1) for _ in range(len(ms))]
res = sum(cs)

for app_index in range(1, len(ms)):
    byte = ms[app_index]
    cost = cs[app_index]

    for capacity in range(1, len(dp[0])):
        if capacity < cost: dp[app_index][capacity] = dp[app_index-1][capacity]
        else:
            dp[app_index][capacity] = max(dp[app_index-1][capacity - cost] + byte, dp[app_index-1][capacity])

        if dp[app_index][capacity] >= M: res = min(res, capacity)

print(res)
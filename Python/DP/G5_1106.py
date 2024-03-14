## G5 1106 호텔
import sys
ip = sys.stdin.readline

## 입력
C, N = map(int, ip().split())
table = [list(map(int, ip().split())) for _ in range(N)]

# DP
DP = [sys.maxsize for _ in range(C+100)]
DP[0] = 0

for cost, people in table:
    for dp_index in range(people, C+100):
        DP[dp_index] = min(DP[dp_index - people] + cost, DP[dp_index])

print(min(DP[C:]))
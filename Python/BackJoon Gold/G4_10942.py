## G4 10942 팰린드롬?
import sys
ip = sys.stdin.readline

##
N = int(ip())
nums = list(map(int, ip().split()))

## DP 진행
dp = [[0]*N for _ in range(N)]

# 규칙 1.
for i in range(N): 
    dp[i][i] = 1

# 규칙 2.
for i in range(N-1):
    if nums[i] == nums[i+1]: 
        dp[i][i+1] = 1

# 규칙 3.
for length in range(2, N):
    for start in range(N - length):
        end = start + length
        if (nums[start] == nums[end]) and (dp[start+1][end-1]):
            dp[start][end] = 1

# 질답 진행
for _ in range(int(ip())):
    S, E = map(lambda x: int(x)-1, ip().split())
    print(dp[S][E])

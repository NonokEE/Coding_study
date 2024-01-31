import sys
ip = sys.stdin.readline

n, k= map(int, ip().split())
things = [(0,0)]

for _ in range(n):
    things.append(tuple(map(int, ip().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = things[i][0]
        v = things[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[n][k])

''' 평범한 배낭
시간 2초 메모리 512MB

N개의 물건이 있고, 각 물건은 무게W와 가치 V를 가진다.
최대 K만큼만 배낭에 넣을 수 있을 때 최대 가치를 출력하셈

- 입력 -
첫 줄에 물건 수 N 1이상 100이하
최대무게 K 1이상 100,000이하
두번째 줄 부터 물건 무게 W랑 가치 V

--1트--: 
그리드네요
무게당 가치 순으로 정렬해서 되는데까지 쑤셔넣으면 됨
이 아니네
그리드로 풀 것 같은데 그리드 아니면 DP지 뭐

오랜만에 하려니 어질어질하네
'''
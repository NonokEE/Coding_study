## G3 1005 ACM Craft
import sys
ip = sys.stdin.readline

##
from collections import deque
for _ in range(int(ip())):
    ## 입력
    N, K = map(int, ip().split())
    D = [0] + list(map(int, ip().split()))

    adj_list = {i:set() for i in range(1, N+1)}
    connect_count = [0] * (N+1)
    
    for _ in range(K):
        X, Y = map(int, ip().split())
        adj_list[X].add(Y)
        connect_count[Y] += 1

    W = int(ip())

    ## 위상 정렬
    queue = deque()
    DP = [0] * (N+1)

    for i in range(1, N+1):
        if connect_count[i] == 0:
            queue.append(i)
            DP[i] = D[i]

    # 진행
    while queue:
        cur = queue.popleft()
        for next in adj_list[cur]:
            connect_count[next] -= 1
            DP[next] = max(DP[next], DP[cur] + D[next])

            if connect_count[next] == 0:
                queue.append(next)

    print(DP[W])

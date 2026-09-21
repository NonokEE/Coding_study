## G3 2252 줄세우기
import sys
ip = sys.stdin.readline

##
N, M = map(int, ip().split())
adj_list = {i:set() for i in range(1, N+1)}
degree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, ip().split())
    adj_list[A].add(B)
    degree[B] += 1

from collections import deque
q = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

res = []
while q:
    cur = q.popleft()
    res.append(cur)

    for next in adj_list[cur]:
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)

print(*res)
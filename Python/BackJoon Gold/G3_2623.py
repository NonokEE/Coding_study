## G3 2623 음악프로그램
import sys
ip = sys.stdin.readline

## 입력
N, M = map(int, ip().split())
adj_list = {i:set() for i in range(1, N+1)}
degree = [0] * (N+1)

for _ in range(M):
    seq = list(map(int, ip().split()))
    for i in range(1, len(seq)-1):
        A, B = seq[i], seq[i+1]
        if B not in adj_list[A]:
            adj_list[A].add(B)
            degree[B] += 1

## 위상 정렬
from collections import deque
q = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

res = []
while q:
    cur = q.popleft()
    res.append(cur)

    for next_node in adj_list[cur]:
        degree[next_node] -= 1
        if degree[next_node] == 0:
            q.append(next_node)

if len(res) < N: print(0)
else:
    for e in res: print(e)
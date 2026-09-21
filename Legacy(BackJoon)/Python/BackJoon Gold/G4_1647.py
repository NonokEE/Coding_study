## G4 1647 도시 분할 계획
import sys
ip = sys.stdin.readline

## 입력
V, E = map(int, ip().split())
adj_list = []
for _ in range(E):
    adj_list.append(list(map(int, ip().split())))
adj_list.sort(key = lambda x:x[2])

## Kruskal Algorithm
parent = list(range(V+1))

def find(n):
    if parent[n] != n: 
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: parent[b] = a
    else    : parent[a] = b

res = 0
longest = 0

for v1, v2, cost in adj_list:
    if find(v1) != find(v2):
        union(v1, v2)
        res += cost
        longest = cost

print(res - longest)

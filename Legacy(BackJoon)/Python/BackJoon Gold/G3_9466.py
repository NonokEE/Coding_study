## G3 9466 텀프로젝트
import sys
ip = sys.stdin.readline

##
sys.setrecursionlimit(200000)

def dfs(x):
    global grouped
    visited[x] = True
    cycle.append(x)
    cur = next_node[x]

    if visited[cur]:
        if cur in cycle:
            grouped += cycle[cycle.index(cur):]
        return
    else:
        dfs(cur)

for _ in range(int(ip())):
    n = int(ip())
    next_node = list(map(lambda x:int(x)-1, ip().split()))
    visited = [False] * n
    grouped = []

    for i in range(n):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(grouped))

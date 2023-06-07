import sys
ip = sys.stdin.readline

N = int(ip())
adj_list = {i:{} for i in range(N)}

for _ in range(N-1):
    parent, child, weight = map(int, ip().split())
    parent -= 1
    child -= 1
    adj_list[parent][child] = weight
    adj_list[child][parent] = weight

def DFS (s):
    stack = [(s, 0)]
    visited = [False for _ in range(N)]

    res = 0
    while stack:
        cur, val = stack.pop()
        
        if val > res:
            res = val

        if not visited[cur]:
            visited[cur] = True
            for child in adj_list[cur].keys():
                if not visited[child]:
                    stack.append((child, val + adj_list[cur][child]))

    return res

vals = [DFS(i) for i in range(N)]
print(max(vals))


''' 트리의 지름
시간 2초 메모리 128MB

가중치 있는 트리 그래프에서 가장 긴 경로를 출력하셈.

- 입력 -
첫 줄에 노드 개수 n, 1이상 10,000이하
둘째줄부터 부모, 자식, 가중치. 가중치는 100이하의 자연수
루트는 항상 1임

- 출력-
트리의 지름을 출력

--2트--:
그래 너무 많아.. 메모리 안걸려도 어차피 시간에서 걸렸을듯
각 노드에 다 돌려서 가장 긴거 찾는건 똑같은데, 알고리즘 자체의 필요조건을 이해하고 있느냐의 차이
플로이드워셜은 너무 자원이 많이 들고, 다익스트라는 너무 오래 걸림.
DFS를 각 노드로 돌려주는게 낫다.

--1트--: 메모리 초과
트리라서 DFS인 척 하는데, 다익스트라로 해결하면 그만 아닌가 싶음.
루트에서 다익스트라 돌린 다음에 1,2번째로 긴거 출력하면 되는거 아닌가?
ㄴㄴ 그게 쫙 펴지는 경우는 아니라서..
모든 노드에서 다익스트라 돌려서 -> 플로이드 워셜
값 제일 큰거 뽑으면 될듯?
이거 안되면 DFS...인데 노드 개수 너무 많아서 플로이드 워셜 힘들지 않나
'''
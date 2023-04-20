###
INF = 99999999

def pmap(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == INF: print("  INF", end=" ")
            else               : print("%5d"%map[i][j], end=" ")
        print()
###


###

import sys
ip = sys.stdin.readline

n = int(ip())
g = []
for i in range(n): g.append(list(map(int, ip().split())))

for temp_node in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][temp_node] and g[temp_node][j]: g[i][j] = 1 

for i in range(n):
    for j in range(n):
        print(g[i][j], end=" ")
    print()

''' 경로 찾기
가중치가 없는 방향 그래프 G가 주어졌을 때, 모든 정점(i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하라

첫 줄에 정점(노드) 개수 N(1개 이상 100개 이하) 둘째 줄 부터 인접행렬을 줍니다

--1트-- : 결과
그니까 빙 돌더라도 갈 수 있냐 없느냐의 문제
일방 통행인 경우도 있음.

플로이드 워셜로 찾으면 될 것 같은데요?
'''
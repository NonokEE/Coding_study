import sys
ip = sys.stdin.readline

T = int(ip())

def DFS(start, farm, cabbage):
    visited = []
    non_visited = [start]
    while non_visited:
        curx, cury = non_visited.pop()       
        cabbage.remove([curx, cury])
        visited.append([curx, cury])
        # LEFT
        if cury < len(farm[0])-1:
            if ([curx, cury+1] not in visited + non_visited) and farm[curx][cury+1] :non_visited.append([curx, cury+1])
        # RIGHT
        if cury > 0:
            if ([curx, cury-1] not in visited + non_visited) and farm[curx][cury-1]:non_visited.append([curx, cury-1])
        # UP
        if curx < len(farm)-1:
            if ([curx+1, cury] not in visited + non_visited) and farm[curx+1][cury]:non_visited.append([curx+1, cury])
        # DOWN
        if curx > 0:
            if ([curx-1, cury] not in visited + non_visited) and farm[curx-1][cury]: non_visited.append([curx-1, cury])

for _ in range(T):
    M, N, K = map(int, ip().split())
    farm = [[0 for _ in range(N)] for _ in range(M)]
    cabbage = []
    count = 0

    for _ in range(K):
        x, y = map(int, ip().split())
        farm[x][y] = 1
        cabbage.append([x,y])

    while cabbage:
        DFS(cabbage[0], farm, cabbage)
        count+=1

    print(count)

''' 유기농 배추
지렁이는 상하좌우 방향으로 이동할 수 있음.
0은 맨땅, 1은 배추땅. 

첫 줄에 TC 개수 T
각 TC마다 M, N, K   (1 <= M, N <= 50) K는 배추 개수
그 아래 K개 줄은 배추 위치. 중복 없음

모든 배추 커버하기 위한 지렁이 최소 개수.

--1트-- : 런타임 에러(Recursion Error)
여기는 너무 크니까 인접 리스트 사용 -> 굳이 안써도 될 수도?
그리고 배추땅 배열도 따로 추가.

일단 첫 땅에 지렁이 심어서 DFS.
탐색한 땅은 배추땅에서 제거.
남은 배추땅으로 가서 또 심고 DFS.
배추땅 길이 0 될때 까지 반복.

--2트-- : 이래도 재귀가 터진다고요?
재귀가 터져버림. DFS에서 일단 보내고 방문 여부 찾지 말고, 방문여부를 먼저 찾고 DFS 보낼지 말지 결정해야 함.
어차피 DFS 시작을 무조건 배추땅에서 하니까, farm 여부도 미리 보고 보내자.

--3트-- : 재귀없이 하니 성공!
탐색 방법을 재귀 안터지게 바꿔야 함. BFS로 구현해봐? 아니면 배추 심어지는 시점에서 인접리스트를 만들어야함.
BFS냐 DFS냐는 별로 안중요한듯. 인접행렬/인접리스트의 시간복잡도가 다르대.

인접행렬 = O(n^2)
인접리스트 = O(n+E)
인접리스트를 구현해보자.

아니면 재귀를 안쓰고 스택으로 하는 방법도 있지 않나?
애초에 지금 인접 행렬을 안쓰고 있음. 재귀 안쓰고 해결하는걸로 해보자.
'''
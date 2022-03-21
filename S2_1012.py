import sys
ip = sys.stdin.readline

T = int(ip())

def DFS(curx, cury, farm, visited, cabbage):
    visited.append([curx, cury])
    cabbage.remove([curx, cury])
    # LEFT
    if curx > 0:
        if ([curx-1, cury] not in visited) and farm[curx-1][cury]: DFS(curx-1, cury, farm, visited, cabbage)
    # RIGHT
    if curx < len(farm)-1:
        if ([curx+1, cury] not in visited) and farm[curx+1][cury]:DFS(curx+1, cury, farm, visited, cabbage)
    # UP
    if cury > 0:
        if ([curx, cury-1] not in visited) and farm[curx][cury-1]:DFS(curx, cury-1, farm, visited, cabbage)
    # DOWN
    if cury < len(farm[0])-1:
        if ([curx, cury+1] not in visited) and farm[curx][cury+1]:DFS(curx, cury+1, farm, visited, cabbage)


for _ in range(T):
    M, N, K = map(int, ip().split())
    farm = [[0 for _ in range(N)] for _ in range(M)]
    visited = []
    cabbage = []
    count = 0

    for _ in range(K):
        x, y = map(int, ip().split())
        farm[x][y] = 1
        cabbage.append([x,y])

    while cabbage:
        DFS(cabbage[0][0], cabbage[0][1], farm, visited, cabbage)
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
'''
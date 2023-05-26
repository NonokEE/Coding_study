import sys 
ip = sys.stdin.readline

N = int(ip())
field = [list(map(int, ip().split())) for _ in range(N)]

#상어 위치 찾기
for i in range(N):
    for j in range(N):
        if field[i][j] == 9:
            sx, sy = i, j

#탐색
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def is_in_field(x,y):
    return (0 <= x < N) and (0 <= y < N)

def seek(sx,sy, shk_size):  #BFS로 경로 맵 생성
    dist = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    q = deque([(sx,sy)])
    visited[sx][sy] = 1
    foods = []    

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            #아직 방문하지 않았고 지나갈 수 있다면 경로로 추가 및 갱신
            if is_in_field(cx, cy) and (visited[cx][cy] == 0) and (field[cx][cy] <= shk_size):  
                q.append((cx,cy))
                visited[cx][cy] = 1
                dist[cx][cy] = dist[x][y] + 1
                
                #해당 경로가 먹을 수 있는 물고기라면 먹이 배열로 추가
                if 0 < field[cx][cy] < shk_size:
                    foods.append((cx,cy,dist[cx][cy]))

    # 거리순, 위, 왼쪽 순으로 정렬하여 반환
    return sorted(foods, key = lambda x: (-x[2], -x[0], -x[1]))

##루프
step = 0
shk_stomach = 0
shk_size = 2
foods = seek(sx ,sy, shk_size)

while foods:
    fx, fy, dist = foods.pop() #다음 먹이의 위치와 거리 
    step += dist
    field[sx][sy] = 0 #상어의 과거 위치를 0으로
    field[fx][fy] = 9 #먹은 먹이의 위치로 상어가 이동
    sx, sy = fx, fy   #상어 위치를 먹이 위치로 갱신

    shk_stomach += 1
    if shk_stomach == shk_size:
        shk_size += 1
        shk_stomach = 0

    foods = seek(sx, sy, shk_size)

print(step)


''' 애기 상어
시간 2초 메모리 512MB

N*N 필드에 물고기 M마리랑 애기상어 1마리가 있다. 한 칸에 물고기는 최대 한 마리
물고기랑 상어는 크기를 가지고 있고, 상어 초기 크기는 2

애기상어는 자기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
자기보다 작은 물고기만 먹을 수 있다.
-> 크기가 같으면 지나갈 수는 있는데 먹을 수는 없다.

상어의 이동 방식
- 더 이상 먹을 수 있는 물고기가 없으면 엄마를 부른다.
- 먹을 수 있는 물고기가 1마리라면 먹으러 간다
- 먹을 수 있는 물고기가 1마리보다 많다면, 가장 가까운 물고기를 먹으러 간다.
  - 가장 가까운게 여러마리라면, 가장 위를 우선.
  - 가장 위도 여러개라면, 왼쪽 우선

애기상어는 1초에 상하좌우로 한 칸씩 이동 가능, 먹는데 따로 시간 안걸림.
자기 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.

공간 줄 태니까, 엄마 안부트로 몇 초 동안 고기를 먹을 수 있는지 구하라.

- 입력 -
첫 줄에 공간크기 N (2이상 20이하)
둘째부터 공간 상태.
0은 빈칸, 1~6은 물고기 크기, 9는 애기상어 위치

--5트--:
BFS하면서 물고기를 한번에 찾네.

--3트--:
먹이들의 좌표도 한번만 알면 된다. 단, 거리가 커질 때 갱신해야한다.
남은 먹이 개수는 상어가 커졌을 때 갱신하면 된다. 매번 갱신할 필요 없음.

--2트--:
로직 자체는 맞는데, 시간 아낄 방법을 생각해보자.
상어가 위치 옮길 때 마다 BFS쓰는 게 좀 비효율적일 것 같음
BFS를 최초 1회만 하고, 그 다음부터는 위치 갱신만 하는게?
근데 그럴라면 일반 필드랑 BFS필드를 합쳐야될 것 같음.

--1트--: 시간초과

게임 AI 짜듯이
while 루프를 짜야할 것 같소

0. 먹을 수 있는게 있는지 탐색(이 때 위치 정보도 받기)
1. 있으면 그 칸까지 이동하는데 걸리는 시간 계산.
 1-1. BFS로 거리 찾으면 됨. 가능하면 그 칸으로 이동
 1-2. 불가능하면 다음 후보 물고기. (후보 물고기를 넣을 때, 제일 왼쪽 제일 위 순으로 넣게 (그냥 루프 돌리면 됨))
2. 먹고 난 후의 뱃속 처리

근데 먹을 수 있는 물고기들 중에서도 가장 가까운거 먹어야되네

1. 먹을 수 있는 물고기들의 좌표 찾기
2. 현재 상어 위치로부터 BFS 진행
3. 먹을 수 있는 좌표들 중 가장 값 작고 우선순위 높은 것을 먹기
4. 지도 갱신

'''
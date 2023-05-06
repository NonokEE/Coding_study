def pfield(arr):
    for line in arr: 
        for e in line:
            if e == 1e9:
                print("%4s"%"INF", end=" ")
            else:
                print("%4d"%e, end= " ")
        print()
    print()
##
import sys
ip = sys.stdin.readline

from collections import deque

n = int(ip())
field = [list(map(int, ip().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

##
# 상어의 좌표, (먹을 수 있는 물고기들 좌표)를 반환
def seek(shk_size):
    res = deque([])
    for i in range(n):
        for j in range(n):
            if (field[i][j] != 0) and (field[i][j] < shk_size):
                res.append((i,j))
            if field[i][j] == 9:
                shark = (i,j)
    return shark, res

# 현재 지도 기반 임시 지도 만들기(큰 물고기를 벽(1e9)으로, 나머지는 무시)
def get_temp_field(shk_size):
    res = []
    for i in range(n):
        line = []
        for j in range(n):
            if   field[i][j] == 9      : line.append(0)
            elif field[i][j] > shk_size: line.append(1e9)
            else                       : line.append(0)
        res.append(line)
    return res

# 범위 안에 있니?
def is_in_field(x, y):
    return (0 <= x < n) and (0 <= y < n)

# BFS 진행하여 결과 필드 반환 (출발점이 2가 되긴 하는데 어차피 먹이 위치는 아니라 상관 없음)
def BFS(depart, shk_size):
    # BFS 전 초기화
    arr = get_temp_field(shk_size)

    step_queue = deque([depart])
    step = 0

    # BFS 시작
    while step_queue:
        temp_queue = deque([])

        while step_queue:
            x, y = step_queue.popleft()

            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]

                if is_in_field(cx,cy) and arr[cx][cy] == 0:
                    arr[cx][cy] = step+1
                    temp_queue.append((cx,cy))

        step_queue = temp_queue    
        step += 1

    return arr
##

#루프 전 초기화
shk_size = 2    #초기 상어 크기 2
shk_stomach = 0 #상어 뱃속 뇸뇸

step = 0        #결과값
shark, dest = seek(shk_size) #초기 상어 위치, 목적지 설정

#루프 시작
while dest: #목적지가 존재하면 루프 진행

    #현재 상어 위치 기반으로 BFS 진행하여 맵 받아오기
    bfs_field = BFS(shark, shk_size) 

    #먹이 후보들까지 가는데 걸리는 거리 산출
    food_distance = []
    for x, y in dest:
        food_distance.append(bfs_field[x][y])

    #가장 가까운 거리의 먹이 먹기 (!)1e9라면 도달 불가능한 먹이
    min_dist = min(food_distance)
    if min_dist == 1e9: #도달 불가능한 경우
        break
    else:
        #먹을 고기의 좌표 찾기
        index = 0
        for i in range(len(food_distance)):
            if food_distance[i] == min_dist:
                index = i
                break
        food_x, food_y = dest[index]    

        #스텝 갱신하고 배 불리기
        step += bfs_field[food_x][food_y]
        shk_stomach += 1
        if shk_stomach == shk_size:
            shk_size += 1
            shk_stomach = 0

        #상어 위치 갱신
        sx, sy = shark

        field[sx][sy] = 0
        field[food_x][food_y] = 9

        #지도 갱신
        shark, dest = seek(shk_size)

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
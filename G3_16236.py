def pfield(arr):
    for line in arr: print(line)
##
import sys
ip = sys.stdin.readline

from collections import deque

INF = 999
n = int(ip())
field = [[[0,0] for _ in range(n)] for _ in range(n)]  #왼쪽 값은 필드 정보, 오른쪽 값은 상어로부터의 거리

# 필드 정보 입력받기
for i in range(n):
    line = list(map(int, ip().split()))
    for j in range(n):
        field[i][j][0] = line[j]
        if line[j] == 9:
            sx, sy = i, j

###
# 상어의 좌표, (먹을 수 있는 물고기들 좌표)를 반환
def seek(shk_size):
    res = deque([])
    for i in range(n):
        for j in range(n):
            if (field[i][j][0] != 0) and (field[i][j][0] < shk_size):
                res.append((i,j))
    return res

# 거리정보 갱신
def set_distance(shk_size, dest):
    #dest = 상어가 도착할 위치의 x,y
    for i in range(n):
        for j in range(n):
            cur = field[i][j][0]
            if cur == 9 :
                field[i][j][1] = 0
            elif cur > shk_size: 
                field[i][j][1] = INF
            else:
                field[i][j][1] = abs(dest[0] - i) + abs(dest[1] - j)
###

# 루프 전 초기화
shk_size = 2
shk_stomach = 0
step = 0

set_distance(shk_size, (sx, sy))
foods = seek(shk_size)

# 루프
while foods: #먹을 수 있는게 있는 동안 루프 진행

    #먹이 후보들까지 가는데 걸리는 거리 산출
    food_distance = []
    for x, y in foods:
        food_distance.append(field[x][y][1])

    #가장 가까운 거리의 먹이 먹기 (!)1e9라면 도달 불가능한 먹이
    min_dist = min(food_distance)
    if min_dist == INF: #도달 불가능한 경우
        break
    else:
        #먹을 고기의 좌표 찾기
        index = 0
        for i in range(len(food_distance)):
            if food_distance[i] == min_dist:
                index = i
                break
        food_x, food_y = foods[index]    

        #스텝 갱신하고 배 불리기
        step += field[food_x][food_y][1]
        shk_stomach += 1
        if shk_stomach == shk_size:
            shk_size += 1
            shk_stomach = 0

        #상어 위치 갱신
        field[sx][sy][0] = 0
        field[food_x][food_y][0] = 9
        sx, sy = food_x, food_y

        #지도 갱신
        set_distance(shk_size, (sx,sy))
        foods = seek(shk_size)

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
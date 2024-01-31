## G3 2206 벽 부수고 이동하기
import sys
ip = sys.stdin.readline

## 입력
INF = 1000000
N, M = map(int, ip().split())
field = [list(map(int, " ".join(ip()).split())) for _ in range(N)]

## 함수
def infield(x, y):
    return (0 <= x < N) and (0 <= y < M)

dx = (1,-1,0,0)
dy = (0,0,-1,1)

## 초기화
from collections import deque

# 첫 차수 = 벽뚫기 여부. 1이면 아직 안뚫고, 0이면 뚫은 것
# 뒤 두개 차수 = 필드 X,Y좌표
queue = deque([(1,0,0)])
res = [[[INF] * M for _ in range(N)] for _ in range(2)]
res[1][0][0] = 1

## DFS 시작
while queue:
    cw, cx, cy = queue.popleft()

    for dir in range(4):
        nx = cx + dx[dir]
        ny = cy + dy[dir]

        if infield(nx,ny) and (res[cw][nx][ny] > res[cw][cx][cy] + 1):
            #길이 없는 경우
            if field[nx][ny]:
                if cw: #벽 뚫기가 가능한 경우에만 진행
                    res[0][nx][ny] = res[cw][cx][cy] + 1
                    queue.append((0,nx,ny))

            #길이 있는 경우
            else:
                res[cw][nx][ny] = res[cw][cx][cy] + 1
                queue.append((cw,nx,ny))

## 출력
val = min(res[0][N-1][M-1], res[1][N-1][M-1])
if val == INF: print(-1)
else         : print(val)


# ##DEBUG
# print()
# print("Non-break")
# for line in res[1]: print(line)

# print()
# print("Break")
# for line in res[0]: print(line)

import sys
ip = sys.stdin.readline

## 입력
HEIGHT, WIDTH = map(int, ip().split())
field = [list(map(int, ip().split())) for _ in range(HEIGHT)]

## 결과 지도 초기화
# 걍 x를 세로로 함
res = [[-1] * WIDTH for _ in range(HEIGHT)] 
for x in range(HEIGHT):
    for y in range(WIDTH):
        if field[x][y] == 2:
            sx, sy = x, y
            res[x][y] = 0 #시작점은 어차피 무조건 큐에 들어가니까 계산하기 좋게 0으로 초기화

        elif field[x][y] == 0:
            res[x][y] = 0 #벽

        elif field[x][y] == 1:
            res[x][y] = -1#미방문한 길

#BFS
def isInField(x,y):
    return (0 <= x < HEIGHT) and (0 <= y < WIDTH)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque
q = deque([(sx, sy)])

while q:
    x, y = q.popleft()

    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]

        #  범위안에 있고,         길이고,                방문 안했으면
        if isInField(cx, cy) and field[cx][cy] == 1 and res[cx][cy] == -1:
            res[cx][cy] = res[x][y] + 1
            q.append((cx,cy))

for line in res: print(*line)



''' 쉬운 최단 거리
시간 1초 메모리 128MB

지도 줄테니까 모든 지점에 대해서 목표지점까지의 거리를 구하라
가로 세로로만 움직일 수 있음

- 입력 -
지도세로크기 n과 가로크기m (둘 다 2이상 1000이하)
다음동안 지도 정보. 0은 벽, 1은 길, 2는 목적지. 입력에서 2는 단 한개.

- 출력-
결과 지도 출력. 
벽은 0으로, 아예 못가는 곳은 -1로 출력.

--1트--: 결과
그냥 BFS같은데.
'''
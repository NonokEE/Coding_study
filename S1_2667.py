def pfield(field:list):
    for i in range(len(field)):
        for j in range(len(field)):
            print("%5s"%str(field[i][j]), end=" ")
        print()
###
import sys
ip = sys.stdin.readline

n = int(ip())
field = [list(map(int, " ".join(ip()).split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if field[i][j]: field[i][j] = "Y"
        else          : field[i][j] = "N"

danji = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for x in range(n):
    for y in range(n):
        if field[x][y] == "N"            : continue #문자열 N인 경우 집이 없는 곳. 탐색할 필요가 없음
        elif type(field[x][y]) == type(0): continue #문자열이 아닌 경우 이미 탐색을 마친 곳. 
        else:
            danji += 1
            field[x][y] = danji

            queue = [(x,y)] #탐색한 적 없는 집일 경우 BFS를 시작하기 위한 큐 생성
            while queue:
                cx, cy = queue.pop(0)

                for i in range(4): #상하좌우
                    nx = cx + dx[i]
                    ny = cy + dy[i]

                    if (0 <= nx < n) and (0 <= ny < n) and (field[nx][ny] == "Y"):
                        queue.append((nx, ny))
                        field[nx][ny] = danji

houses = []
for dval in range(1, danji+1):
    cnt = 0
    for line in field:
        cnt += line.count(dval)
    houses.append(cnt)
houses.sort()

print(danji)
for res in houses: print(res)
''' 단지번호붙이기
정사각형 지도 있습니다.
1은 집이 있는 곳, 0은 집이 없는 곳.
지도에서 집이 연결되어 있으면 '단지'라고 부른다. 상하좌우로 접해있는 경우만 연결이다.
지도 안의 단지 수와, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하세요.

- 입력 -
첫 줄에 지도의 변의 길이 N (5이상 25이하)
이후 지도 정보

--1트--: 이게 되네 ㅋㅋㅋㅋ
BFS일 것으로 예상됩니다. DFS로도 가능은 한데, BFS가 더 효율적일 것 같음

초기 지도상에는 0, 1로 들어오는데 
-> 1단지 2단지 ...로 구분해주고 싶으니까 지도를 False True로 하자 
-> True가 1이랑 ==이라서 문자열로 구분하는게 나을듯

단지가 중간중간 끊겨있기 때문에 루트에서 서치 돌리면 무조건 끊어짐
-> 모든 노드를 다 검사해야됨
-> 'Y'면 아직 방문하지 않은 단지
-> 방문한 단지는 숫자로 바꿈
따라서 모든 노드에 대해서 검사를 하되, 방문 여부를 처음에 파악해서 거르도록 함

BFS가 한번 가동됐을 때는 같은 카운터를 유지해줘야함.

미쳐버린 4중 반복문
시간제한 1초밖에 안되는데 이걸로 가능하려나...
맵 크기가 최대 25니까 가능할 것 같기도 하고

'''
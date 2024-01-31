import sys
ip = sys.stdin.readline

n = int(ip())
field_RGB = []
for _ in range(n):
    field_RGB.append(list(ip().strip()))

field_CW = []
for line in field_RGB:
    field_CW.append(line[:])

for i in range(n):
    for j in range(n):
        if field_CW[i][j] == 'G':
            field_CW[i][j] = 'R'

dx = [0,0,-1,1]
dy = [-1,1,0,0]

count_RGB = 0
count_CW = 0

def is_in_field(x,y):
    return (0 <= x < n) and (0 <= y < n)

for i in range(n):
    for j in range(n):
        #정상 필드
        if type(field_RGB[i][j]) == type("str"): # 문자열인 경우 = 아직 탐색 안한 경우. 탐색 했으면 정수로 갱신됨
            count_RGB += 1
            stack = [(i,j)]
            color_current = field_RGB[i][j]
            field_RGB[i][j] = count_RGB

            while stack:
                x,y = stack.pop()
                
                for direction in range(4):
                    nx = x + dx[direction]
                    ny = y + dy[direction]

                    if is_in_field(nx,ny) and (field_RGB[nx][ny] == color_current):
                        stack.append((nx,ny))
                        field_RGB[nx][ny] = count_RGB

        #색약 필드
        if type(field_CW[i][j]) == type("str"): 
            count_CW += 1
            stack = [(i,j)]
            color_current = field_CW[i][j]
            field_CW[i][j] = count_CW

            while stack:
                x,y = stack.pop()
                
                for direction in range(4):
                    nx = x + dx[direction]
                    ny = y + dy[direction]

                    if is_in_field(nx,ny) and (field_CW[nx][ny] == color_current):
                        stack.append((nx,ny))
                        field_CW[nx][ny] = count_CW
        
print(count_RGB, count_CW)

''' 적록색약
시간 1초 메모리 128MB

N*N 그리드에 R G B가 하나씩 있다.
그리고 구역 단위로 뭉탱이로 같은 색으로 돼있음.

정상인이 봤을 때(R,G,B 따로 취급할 때) 구역의 개수와
적록색약이 봤을 때(RG,B로 취급할 때) 구역의 개수를 출력하셈

- 입력 -
첫 줄에 N
둘째 줄 부터 그림

--1트--: 성공
그냥 뭐 탐색 굴리면 되겠네요. 
'''
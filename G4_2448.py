import sys
ip = sys.stdin.readline

height = int(ip())

#k 파악
kdict = [0 for _ in range(11)]
kdict[0] = 3
for i in range(1,11):
    kdict[i] = 2*kdict[i-1]
k = kdict.index(height)

#바닥 개수 파악
floorDict = [0 for _ in range(11)]
floorDict[0] = 5
for i in range(1,11):
    floorDict[i] = floorDict[i-1]*2 + 1
floor = floorDict[k]

#보드 생성 및 왕삼각형 만들기
board = [[" " for _ in range(floor)] for _ in range(height)]
for lv in range(height):
    s = floor//2 - lv
    e = floor//2 + lv + 1
    for i in range(s, e):
        board[lv][i] = "*"

#삼각형 파내기
def carve(s, e, c, k):    #대상 삼각형의 시작레벨, 끝레벨, 대상 삼각형의 가운데 좌표
    if k: 
        h = e-s
        for lv in range(s + h//2, e):
            w = h - lv - 1 + s
            l = c - w
            r = c + w + 1
            for i in range(l, r):
                board[lv][i] = " "

        k -= 1
        carve(s, s + h//2, c, k)
        carve(s + h//2, e, c - kdict[k], k)
        carve(s + h//2, e, c + kdict[k], k)
    else:
        board[s+1][c] = " "
        return

carve(0, height, floor//2, k)

#출력 함수
def pboard(arr):
    for line in arr:
        for e in line:
            print(e, end="")
        print()

pboard(board)



''' 별 찍기 - 11
시간 1초 메모리 256MB

규칙 알아서 파악하고 찍으셈 ㅋㅋ

- 입력 -
첫 줄에 N이 주어짐. 
N은 항상 3 * 2^k
k는 0이상 10이하

- 출력-
별 출력

--1트--: 결과
이거 1학년때 과제로 나왔던거같은데..
가능한 입력: 3, 6, 12, 24, 48, 96, 192, 

각 입력의 수가 높이와 같다.
바닥은 점화식으로 구했고
k는 log 쓸 수가 없어서 점화식으로 구해야됨

논리식으로 별 찍을지 말지 못정하나?
이런 문제는 1단 2단만 해결하면 해결됨

시간은 별로 안빡빡함.
출력하면서 할게 아니라 삼각형을 먼저 만들어놓고 가운데를 파야되니까, 배열을 만들어놔? 출력시간이 좀 짜증나지긴 한데
'''
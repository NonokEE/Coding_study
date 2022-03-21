import sys
ip = sys.stdin.readline

N = int(ip())
original = [list(map(int, ip().split())) for _ in range(N)]

def cut(n, paper, white, blue):
    tot = 0
    for i in range(n):
        tot += sum(paper[i])

    if tot == 0:
        white += 1
    elif tot == n**2:
        blue += 1
    else:
        p1 = [paper[i][:int(n/2)] for i in range(int(n/2))]
        p2 = [paper[i][int(n/2):] for i in range(int(n/2))]
        p3 = [paper[i][:int(n/2)] for i in range(int(n/2), n)]
        p4 = [paper[i][int(n/2):] for i in range(int(n/2), n)]
        p1white, p1blue = cut(int(n/2), p1, blue, white)
        p2white, p2blue = cut(int(n/2), p2, blue, white)
        p3white, p3blue = cut(int(n/2), p3, blue, white)
        p4white, p4blue = cut(int(n/2), p4, blue, white)

        white = p1white + p2white + p3white + p4white
        blue = p1blue + p2blue + p3blue + p4blue

    return [white, blue]


white, blue = cut(N, original, 0, 0)
print(white)
print(blue)

''' 색종이 만들기
정사각형 모양 종이(n*n 행렬)이 있음. 1이면 파란색, 0이면 하얀색.
얘를 잘라서 다양한 크기의 하얀색 혹은 파란색 정사각형 종이를 만들거야.

종이 자르는 규칙
모두 같은 색이면 통과
아니라면 가로 세로 중앙 잘라서 4등분
  작은 종이에도 똑같이 적용

한 변의 길이가 N인 정사각형과 칸의 내용이 주어질 때, 결과물 하얀 종이랑 파란 종이 개수를 구해라.
N은 2^n (1<=n<=7), 입력으로 2차원 배열 줌. 
하얀색, 파란색 순으로 출력.

--1트-- : 성공!
브루트 포스? 큰 종이에서 잘라보자.
안되면 작은 종이에서 역으로 올라가보자.
! numpy를 안쓰고 바닐라 array는 2차원 배열 슬라이싱이 안된다.
'''